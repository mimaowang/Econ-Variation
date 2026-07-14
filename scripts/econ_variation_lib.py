from __future__ import annotations

import ipaddress
import json
import os
import re
import socket
import time
import uuid
from contextlib import contextmanager
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import parse_qsl, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
VARIATION_DIR = ROOT / "variations"
STATE_DIR = ROOT / "state"
SCHEMA_PATH = ROOT / "schema" / "variation.schema.json"
TOPICS_PATH = ROOT / "schema" / "topics.yaml"
PLACEHOLDER_URLS = {"", "needs-verification", "n/a", "none", "null"}
SENSITIVE_QUERY_KEYS = {"api_key", "apikey", "auth", "key", "password", "secret", "sig", "signature", "token"}


@dataclass(frozen=True)
class VariationRecord:
    path: Path
    data: dict[str, Any]
    body: str

    @property
    def id(self) -> str:
        return str(self.data.get("id", "")).strip()

    @property
    def status(self) -> str:
        return str(self.data.get("status", "")).strip()


def read_frontmatter(path: Path) -> VariationRecord:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|\Z)", text, re.DOTALL)
    if not match:
        raise ValueError("valid YAML frontmatter delimiters were not found")
    value = yaml.safe_load(match.group(1))
    if not isinstance(value, dict):
        raise ValueError("frontmatter must decode to a mapping")
    return VariationRecord(path=path, data=value, body=text[match.end() :])


def load_records() -> tuple[list[VariationRecord], list[tuple[Path, str]]]:
    records: list[VariationRecord] = []
    failures: list[tuple[Path, str]] = []
    for path in sorted(VARIATION_DIR.glob("*.md"), key=lambda item: item.name.casefold()):
        if path.name == "template.md":
            continue
        try:
            records.append(read_frontmatter(path))
        except Exception as exc:
            failures.append((path, str(exc)))
    return records, failures


def read_jsonl(path: Path) -> tuple[list[dict[str, Any]], list[str]]:
    if not path.exists():
        return [], ["file does not exist"]
    rows: list[dict[str, Any]] = []
    errors: list[str] = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
            if not isinstance(row, dict):
                raise ValueError("row is not an object")
            rows.append(row)
        except Exception as exc:
            errors.append(f"line {number}: {exc}")
    return rows, errors


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        temporary.write_text(text, encoding="utf-8", newline="\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2, default=str) + "\n")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    atomic_write_text(path, "".join(json.dumps(row, ensure_ascii=False, default=str) + "\n" for row in rows))


def normalize_identity(value: str) -> str:
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", value.casefold())


@lru_cache(maxsize=1)
def load_topic_taxonomy() -> dict[str, list[str]]:
    value = yaml.safe_load(TOPICS_PATH.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("schema_version") != 1 or not isinstance(value.get("topics"), dict):
        raise ValueError("schema/topics.yaml is invalid")
    taxonomy: dict[str, list[str]] = {}
    for topic, definition in value["topics"].items():
        aliases = definition.get("aliases") if isinstance(definition, dict) else None
        if not isinstance(topic, str) or not isinstance(aliases, list) or not aliases:
            raise ValueError(f"invalid topic definition: {topic}")
        taxonomy[topic] = [topic, *(str(alias) for alias in aliases)]
    return taxonomy


def canonical_topics(values: Iterable[Any], *, substring: bool = False) -> list[str]:
    taxonomy = load_topic_taxonomy()
    normalized_values = [normalize_identity(str(value)) for value in values if str(value or "").strip()]
    matches: set[str] = set()
    for topic, aliases in taxonomy.items():
        normalized_aliases = {normalize_identity(alias) for alias in aliases}
        if any(
            value == alias or (substring and alias and alias in value)
            for value in normalized_values
            for alias in normalized_aliases
        ):
            matches.add(topic)
    return sorted(matches)


def identity_fingerprint(data: dict[str, Any]) -> str:
    identity = data.get("identity") if isinstance(data.get("identity"), dict) else {}
    scope = data.get("scope") if isinstance(data.get("scope"), dict) else {}
    parts = [
        identity.get("authority", ""), identity.get("instrument", ""),
        " ".join(identity.get("legal_identifiers", []) or []),
        scope.get("country", ""), " ".join(scope.get("regions", []) or []),
        identity.get("implementation_regime", ""), identity.get("assignment_mechanism", ""),
    ]
    return "|".join(normalize_identity(str(part)) for part in parts)


def knowledge_eligibility(data: dict[str, Any]) -> str:
    """Return static knowledge readiness; query-specific fit is evaluated elsewhere."""
    status = str(data.get("status", ""))
    scope = data.get("scope") if isinstance(data.get("scope"), dict) else {}
    role = scope.get("knowledge_role")
    if status in {"contested", "deprecated"}:
        return "do-not-recommend"
    if role == "transferable-method":
        managed = (data.get("provenance") or {}).get("task_id") != "legacy-untracked"
        if status in {"grounded", "design-documented"} or (status == "extracted" and managed):
            return "method-inspiration"
        return "method-lead"
    if status == "design-documented":
        return "direct-candidate"
    if status == "grounded":
        return "conditional-candidate"
    return "lead-only"


def public_url_issues(value: Any) -> list[str]:
    text = str(value or "").strip()
    if text.casefold() in PLACEHOLDER_URLS:
        return []
    issues: set[str] = set()
    try:
        parsed = urlsplit(text)
    except ValueError:
        return ["invalid-url"]
    if parsed.scheme.casefold() not in {"http", "https"}:
        issues.add("non-http-scheme")
    if not parsed.hostname:
        issues.add("missing-host")
    if parsed.username or parsed.password:
        issues.add("userinfo-not-allowed")
    query_keys = {key.casefold() for key, _ in parse_qsl(parsed.query, keep_blank_values=True)}
    if query_keys & SENSITIVE_QUERY_KEYS:
        issues.add("sensitive-query-parameter")
    if parsed.hostname:
        host = parsed.hostname.casefold().rstrip(".")
        if host in {"example.com", "example.org", "example.net"} or host.endswith(
            (".example.com", ".example.org", ".example.net")
        ):
            issues.add("placeholder-host")
        if host == "localhost" or host.endswith((".local", ".internal", ".localhost")):
            issues.add("local-hostname")
        try:
            address = ipaddress.ip_address(host)
        except ValueError:
            address = None
        if address is not None and not address.is_global:
            issues.add("non-public-ip")
    return sorted(issues)


def _process_alive(pid: Any) -> bool:
    try:
        value = int(pid)
    except (TypeError, ValueError):
        return False
    if value <= 0:
        return False
    if os.name == "nt":
        try:
            import ctypes

            handle = ctypes.windll.kernel32.OpenProcess(0x1000, False, value)
            if not handle:
                return False
            ctypes.windll.kernel32.CloseHandle(handle)
            return True
        except (AttributeError, OSError):
            return False
    try:
        os.kill(value, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


@contextmanager
def workspace_lock(name: str, stale_seconds: int = 3600):
    path = STATE_DIR / f".{name}.lock"
    token = uuid.uuid4().hex
    payload = {"token": token, "pid": os.getpid(), "host": socket.gethostname(), "created": time.time()}
    while True:
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                json.dump(payload, handle)
            break
        except FileExistsError:
            existing: dict[str, Any] = {}
            try:
                age = time.time() - path.stat().st_mtime
            except OSError:
                age = 0
            try:
                existing = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                existing = {}
            if age > stale_seconds and not (
                existing.get("host") == socket.gethostname() and _process_alive(existing.get("pid"))
            ):
                path.unlink(missing_ok=True)
                continue
            raise RuntimeError(f"workspace is locked: {path}")
    try:
        yield
    finally:
        try:
            if json.loads(path.read_text(encoding="utf-8")).get("token") == token:
                path.unlink()
        except FileNotFoundError:
            pass
