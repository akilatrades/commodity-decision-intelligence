"""Small runtime health check used by the project smoke test."""


def get_project_status() -> dict[str, str]:
    """Return a deterministic status payload for smoke testing."""
    return {
        "name": "commodity-decision-intelligence",
        "status": "ok",
        "stage": "step-2-controlled-sample-data",
    }
