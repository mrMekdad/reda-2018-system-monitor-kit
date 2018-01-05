"""Core workflow for System Monitor Kit by Red@."""

PROJECT_NAME = "System Monitor Kit"
DOMAIN_THEME = "software engineering"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
