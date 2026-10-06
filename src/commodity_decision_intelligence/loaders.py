"""CSV loaders for controlled prototype inputs.

Step 2 assumes the committed sample files are well-formed. Explicit business
validation is introduced in Roadmap Step 5. Parsing here is deliberately small
and deterministic so the raw CSV fields map visibly into typed records.
"""

from csv import DictReader
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Iterable

from commodity_decision_intelligence.models import (
    FuturesHedge,
    PhysicalExposure,
    SampleDataset,
    Scenario,
)

PathLike = str | Path


def _read_rows(path: PathLike) -> Iterable[dict[str, str]]:
    """Yield rows from a UTF-8 CSV file."""
    with Path(path).open("r", encoding="utf-8", newline="") as handle:
        yield from DictReader(handle)


def load_physical_exposures(path: PathLike) -> tuple[PhysicalExposure, ...]:
    """Load physical exposure records from CSV."""
    records = []
    for row in _read_rows(path):
        records.append(
            PhysicalExposure(
                exposure_id=row["exposure_id"],
                business_unit=row["business_unit"],
                commodity=row["commodity"],
                location=row["location"],
                delivery_month=date.fromisoformat(row["delivery_month"]),
                volume=Decimal(row["volume"]),
                volume_unit=row["volume_unit"],
                reference_price=Decimal(row["reference_price"]),
                currency=row["currency"],
                source_type=row["source_type"],
                source_name=row["source_name"],
            )
        )
    return tuple(records)


def load_futures_hedges(path: PathLike) -> tuple[FuturesHedge, ...]:
    """Load futures hedge records from CSV."""
    records = []
    for row in _read_rows(path):
        records.append(
            FuturesHedge(
                hedge_id=row["hedge_id"],
                business_unit=row["business_unit"],
                commodity=row["commodity"],
                hedge_instrument=row["hedge_instrument"],
                contract_month=date.fromisoformat(row["contract_month"]),
                direction=row["direction"],
                contracts=int(row["contracts"]),
                contract_multiplier=Decimal(row["contract_multiplier"]),
                volume_unit=row["volume_unit"],
                reference_futures_price=Decimal(row["reference_futures_price"]),
                currency=row["currency"],
                source_type=row["source_type"],
                source_name=row["source_name"],
            )
        )
    return tuple(records)


def load_scenarios(path: PathLike) -> tuple[Scenario, ...]:
    """Load scenario records from CSV."""
    records = []
    for row in _read_rows(path):
        records.append(
            Scenario(
                scenario_id=row["scenario_id"],
                scenario_name=row["scenario_name"],
                commodity=row["commodity"],
                price_shock=Decimal(row["price_shock"]),
                price_unit=row["price_unit"],
                source_type=row["source_type"],
                source_name=row["source_name"],
            )
        )
    return tuple(records)


def load_sample_dataset(directory: PathLike) -> SampleDataset:
    """Load all controlled Step 2 sample files from one directory."""
    base = Path(directory)
    return SampleDataset(
        physical_exposures=load_physical_exposures(base / "physical_exposure.csv"),
        futures_hedges=load_futures_hedges(base / "futures_hedges.csv"),
        scenarios=load_scenarios(base / "scenarios.csv"),
    )
