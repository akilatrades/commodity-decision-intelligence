"""Allow the package to be run with: python -m commodity_decision_intelligence."""

from commodity_decision_intelligence.health import get_project_status


def main() -> None:
    """Print a simple confirmation that the package is runnable."""
    status = get_project_status()
    print(
        f"{status['name']} | status={status['status']} | stage={status['stage']}"
    )


if __name__ == "__main__":
    main()
