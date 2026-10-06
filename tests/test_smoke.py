"""Smoke tests for the project skeleton."""

from commodity_decision_intelligence import __version__
from commodity_decision_intelligence.health import get_project_status


def test_package_version() -> None:
    assert __version__ == "0.1.0"


def test_project_status_is_deterministic() -> None:
    assert get_project_status() == {
        "name": "commodity-decision-intelligence",
        "status": "ok",
        "stage": "step-1-project-skeleton",
    }
