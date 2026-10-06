"""Tests proving that the controlled Step 2 inputs load exactly."""

from datetime import date
from decimal import Decimal
from pathlib import Path

from commodity_decision_intelligence.loaders import load_sample_dataset

SAMPLE_DATA = Path(__file__).resolve().parents[1] / "data" / "sample"


def test_sample_dataset_loads_expected_record_counts() -> None:
    dataset = load_sample_dataset(SAMPLE_DATA)

    assert len(dataset.physical_exposures) == 1
    assert len(dataset.futures_hedges) == 1
    assert len(dataset.scenarios) == 1


def test_physical_exposure_fields_are_preserved() -> None:
    exposure = load_sample_dataset(SAMPLE_DATA).physical_exposures[0]

    assert exposure.exposure_id == "EXP-WTI-001"
    assert exposure.business_unit == "Crude Production"
    assert exposure.commodity == "WTI"
    assert exposure.location == "Cushing, OK"
    assert exposure.delivery_month == date(2026, 11, 1)
    assert exposure.volume == Decimal("100000")
    assert exposure.volume_unit == "bbl"
    assert exposure.reference_price == Decimal("70.00")
    assert exposure.currency == "USD"
    assert exposure.source_type == "synthetic"
    assert exposure.source_name == "controlled_sample"


def test_futures_hedge_fields_are_preserved() -> None:
    hedge = load_sample_dataset(SAMPLE_DATA).futures_hedges[0]

    assert hedge.hedge_id == "HEDGE-WTI-001"
    assert hedge.business_unit == "Crude Production"
    assert hedge.commodity == "WTI"
    assert hedge.hedge_instrument == "NYMEX WTI Futures"
    assert hedge.contract_month == date(2026, 11, 1)
    assert hedge.direction == "short"
    assert hedge.contracts == 75
    assert hedge.contract_multiplier == Decimal("1000")
    assert hedge.volume_unit == "bbl"
    assert hedge.reference_futures_price == Decimal("70.00")
    assert hedge.currency == "USD"
    assert hedge.source_type == "synthetic"
    assert hedge.source_name == "controlled_sample"


def test_scenario_fields_are_preserved() -> None:
    scenario = load_sample_dataset(SAMPLE_DATA).scenarios[0]

    assert scenario.scenario_id == "SCN-WTI-DOWN-10"
    assert scenario.scenario_name == "WTI down 10 USD per bbl"
    assert scenario.commodity == "WTI"
    assert scenario.price_shock == Decimal("-10.00")
    assert scenario.price_unit == "USD/bbl"
    assert scenario.source_type == "synthetic"
    assert scenario.source_name == "controlled_sample"
