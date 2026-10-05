"""Configure only the operational environment, not models or developer tools."""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parents[1]


def configure(root: Path) -> None:
    environment = root / ".venv"
    python = environment / ("Scripts/python.exe" if sys.platform == "win32" else "bin/python")
    if not python.exists():
        venv.EnvBuilder(with_pip=True).create(environment)
    subprocess.run(
        [str(python), "-m", "pip", "install", "-r", str(root / "requirements.txt")],
        cwd=root, check=True,
    )
    subprocess.run([str(python), "scripts/doctor.py"], cwd=root, check=True)
    print(f"Ready: open {root} in your agent. Tools use {python}")
    print("No developer dependencies installed. Read AGENTS.md to start.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, help="Export a Git checkout into a new runtime-only folder")
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        parser.error("Python 3.10 or newer is required.")
    root = ROOT
    if args.destination:
        from runtime_bundle import copy_runtime

        root = args.destination.resolve()
        copy_runtime(root)
    configure(root)


if __name__ == "__main__":
    main()
