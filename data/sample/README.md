# Controlled Sample Data

This directory contains the synthetic inputs used to prove the first Commodity
Decision Intelligence workflow.

The records are **invented for testing**. They are not historical market data,
customer data, or trading recommendations.

## Business story

The fictional `Crude Production` business unit expects to produce:

- 100,000 barrels of WTI-linked crude,
- for November 2026,
- with a $70.00/bbl reference price.

The business has hedged part of that exposure with:

- 75 short NYMEX WTI futures contracts,
- 1,000 barrels per contract,
- representing 75,000 barrels of hedge volume.

A controlled scenario then asks what would happen if WTI moved down by
$10.00/bbl.

No financial-impact calculation is performed in Step 2. This step only proves
that the inputs can be loaded into typed Python records without losing their
meaning.

## Files

### `physical_exposure.csv`

| Field | Sample value | Meaning |
|---|---|---|
| exposure_id | EXP-WTI-001 | Unique physical exposure identifier |
| business_unit | Crude Production | Fictional portfolio/business unit |
| commodity | WTI | Commodity reference |
| location | Cushing, OK | Exposure location |
| delivery_month | 2026-11-01 | ISO date representing the delivery month |
| volume | 100000 | Physical quantity |
| volume_unit | bbl | Barrels |
| reference_price | 70.00 | Starting price assumption |
| currency | USD | Reporting currency |
| source_type | synthetic | Data classification |
| source_name | controlled_sample | Lineage/source label |

### `futures_hedges.csv`

| Field | Sample value | Meaning |
|---|---|---|
| hedge_id | HEDGE-WTI-001 | Unique hedge identifier |
| business_unit | Crude Production | Business unit linked to the hedge |
| commodity | WTI | Commodity reference |
| hedge_instrument | NYMEX WTI Futures | Hedge instrument label |
| contract_month | 2026-11-01 | ISO date representing the futures month |
| direction | short | Hedge direction |
| contracts | 75 | Number of futures contracts |
| contract_multiplier | 1000 | Barrels represented by one contract |
| volume_unit | bbl | Hedge quantity unit |
| reference_futures_price | 70.00 | Starting futures-price assumption |
| currency | USD | Reporting currency |
| source_type | synthetic | Data classification |
| source_name | controlled_sample | Lineage/source label |

### `scenarios.csv`

| Field | Sample value | Meaning |
|---|---|---|
| scenario_id | SCN-WTI-DOWN-10 | Unique scenario identifier |
| scenario_name | WTI down 10 USD per bbl | Human-readable scenario |
| commodity | WTI | Commodity affected |
| price_shock | -10.00 | Flat-price change |
| price_unit | USD/bbl | Unit of the price shock |
| source_type | synthetic | Data classification |
| source_name | controlled_sample | Lineage/source label |

## Why the source fields matter

Even synthetic records carry `source_type` and `source_name`. This starts the
lineage chain early:

```text
Future analytical result
        ↓
Typed input record
        ↓
CSV row
        ↓
source_type + source_name
```

Later enterprise integrations can replace the CSV source without changing the
meaning of the analytical record.

## Repository rule

Only synthetic or otherwise approved non-restricted data may be committed to
this directory. Do not add customer data, API keys, confidential exports, or
restricted market data.
