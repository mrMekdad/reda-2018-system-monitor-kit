import argparse
from system_monitor_kit.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Terminal-first monitor for processes, snapshots, and CSV reports.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
