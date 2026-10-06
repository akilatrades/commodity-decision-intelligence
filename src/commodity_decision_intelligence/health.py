"""Small runtime health check used by the Step 1 project skeleton."""


def get_project_status() -> dict[str, str]:
    """Return a deterministic status payload for smoke testing."""
    return {
        "name": "commodity-decision-intelligence",
        "status": "ok",
        "stage": "step-1-project-skeleton",
    }
