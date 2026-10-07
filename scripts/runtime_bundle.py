"""Export operational files from tracked source, without a second knowledge base."""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RUNTIME_DIRS = {"variations", "sources", "state", "schema", "guides", "dist", "scripts", "assets"}
RUNTIME_FILES = {"README.md", "AGENTS.md", "LICENSE", "SECURITY.md", "requirements.txt", ".gitignore"}


def runtime_paths(root: Path = ROOT) -> list[str]:
    tracked = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True,
    ).stdout.decode("utf-8").split("\0")
    return sorted(path for path in tracked if path and (
        path in RUNTIME_FILES or path.split("/", 1)[0] in RUNTIME_DIRS
    ))


def copy_runtime(destination: Path, root: Path = ROOT) -> None:
    if destination.exists() and any(destination.iterdir()):
        raise ValueError("Choose a new or empty destination; existing files are not overwritten.")
    paths = runtime_paths(root)
    destination.mkdir(parents=True, exist_ok=True)
    for relative in paths:
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((root / relative).read_bytes())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="New runtime ZIP path")
    args = parser.parse_args()
    paths = runtime_paths()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "x", compression=zipfile.ZIP_DEFLATED) as bundle:
        for relative in paths:
            bundle.write(ROOT / relative, "Econ-Variation/" + relative)
    print(f"Runtime bundle: {args.output} ({len(paths)} files; no tests or benchmarks)")


if __name__ == "__main__":
    main()
