from __future__ import annotations

import re
import subprocess
import sys
from datetime import datetime


VERSION_RE = re.compile(r"^version=(.+)$", re.MULTILINE)
DATE_RE = re.compile(r"^lastUpdated=(.+)$", re.MULTILINE)
ZERO_SHA = "0" * 40


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout


def read_version_file(commitish: str) -> str | None:
    result = subprocess.run(
        ["git", "show", f"{commitish}:version.txt"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    return result.stdout


def parse_version_fields(content: str) -> tuple[str, str]:
    version_match = VERSION_RE.search(content)
    date_match = DATE_RE.search(content)
    if not version_match or not date_match:
        raise SystemExit(
            "Push blocked: version.txt must contain both 'version=' and 'lastUpdated=' lines."
        )
    return version_match.group(1).strip(), date_match.group(1).strip()


def changed_in_commit(commitish: str) -> bool:
    changed = git("diff-tree", "--root", "--no-commit-id", "--name-only", "-r", commitish, "--", "version.txt")
    return "version.txt" in changed.splitlines()


def parent_commit(commitish: str) -> str | None:
    parents = git("rev-list", "--parents", "-n", "1", commitish).strip().split()
    if len(parents) > 1:
        return parents[1]
    return None


def validate_commit(commitish: str) -> None:
    if commitish == ZERO_SHA:
        return

    if not changed_in_commit(commitish):
        raise SystemExit(
            "Push blocked: the commit being pushed must update version.txt before pushing."
        )

    current_content = read_version_file(commitish)
    if current_content is None:
        raise SystemExit("Push blocked: version.txt must exist in the commit being pushed.")
    current_version, current_date = parse_version_fields(current_content)

    parent = parent_commit(commitish)
    if parent:
        previous_content = read_version_file(parent)
        if previous_content is not None:
            previous_version, _ = parse_version_fields(previous_content)
            if current_version == previous_version:
                raise SystemExit(
                    "Push blocked: version.txt was changed, but the version number was not bumped."
                )

    try:
        parsed_date = datetime.fromisoformat(current_date)
    except ValueError as exc:
        raise SystemExit(
            "Push blocked: lastUpdated must be an ISO timestamp like 2026-04-16T16:53:37."
        ) from exc

    today = datetime.now().date()
    if parsed_date.date() != today:
        raise SystemExit(
            f"Push blocked: lastUpdated must use today's date ({today.isoformat()})."
        )


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: check_version_on_push.py <commit-sha>")
    validate_commit(sys.argv[1])


if __name__ == "__main__":
    main()
