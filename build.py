import subprocess
import sys

from scripts.version_manager import update_version


def build_executable():
    new_version = update_version()
    subprocess.run([
        "python", "-m", "nuitka",
        "--windows-console-mode=disable",
        "--windows-icon-from-ico=assets/ManualSearch.ico",
        "--include-data-file=utils/config.ini=config.ini",
        "--include-data-dir=templates=templates",
        "--output-filename=ManualSearch.exe",
        "main.py"
    ])

    print(f"Executable built successfully. Version: {new_version}")
    return new_version


if __name__ == "__main__":
    build_executable()