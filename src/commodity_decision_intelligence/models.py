"""Typed records used by the controlled prototype inputs.

These models describe data only. Business calculations are intentionally kept
out of this module so loading, validation, calculation, and reporting can
remain separate layers.
"""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class PhysicalExposure:
    """One physical commodity exposure record."""

    exposure_id: str
    business_unit: str
    commodity: str
    location: str
    delivery_month: date
    volume: Decimal
    volume_unit: str
    reference_price: Decimal
    currency: str
    source_type: str
    source_name: str


@dataclass(frozen=True)
class FuturesHedge:
    """One futures hedge record."""

    hedge_id: str
    business_unit: str
    commodity: str
    hedge_instrument: str
    contract_month: date
    direction: str
    contracts: int
    contract_multiplier: Decimal
    volume_unit: str
    reference_futures_price: Decimal
    currency: str
    source_type: str
    source_name: str


@dataclass(frozen=True)
class Scenario:
    """One controlled market scenario."""

    scenario_id: str
    scenario_name: str
    commodity: str
    price_shock: Decimal
    price_unit: str
    source_type: str
    source_name: str


@dataclass(frozen=True)
class SampleDataset:
    """The three controlled input groups used by the first prototype."""

    physical_exposures: tuple[PhysicalExposure, ...]
    futures_hedges: tuple[FuturesHedge, ...]
    scenarios: tuple[Scenario, ...]
