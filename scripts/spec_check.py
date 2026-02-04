from pathlib import Path

REQUIRED_FILES = [
    "specs/_meta.md",
    "specs/functional.md",
    "specs/technical.md",
]


def main() -> None:
    missing = [p for p in REQUIRED_FILES if not Path(p).exists()]
    if missing:
        raise SystemExit(f"Missing required spec files: {missing}")

    print("Spec check passed.")


if __name__ == "__main__":
    main()
