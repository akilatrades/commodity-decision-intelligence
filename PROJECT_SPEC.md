# Project Specification

## 1. Product purpose

Commodity firms often make decisions using information spread across positions, hedges, market data, spreadsheets, internal reports, and operational assumptions.

This project aims to build an analytical layer that can combine those inputs and answer questions such as:

- What is the company exposed to?
- How much of that exposure is hedged?
- What happens under a specified market scenario?
- Which part of the portfolio drives the result?
- What assumptions produced the answer?

The long-term goal is a **Commodity Decision Intelligence Platform**.

The product is being **designed for enterprise workflows from the beginning**, but the first implementation is deliberately narrow so the analytical core can be proven before enterprise integrations are added.

---

## 2. Initial enterprise user

The first design target is a **crude Market Risk / Supply & Trading Analytics team inside a large energy or commodity enterprise**.

The likely first internal users are people responsible for:

- physical and financial exposure,
- hedge coverage,
- stress and scenario analysis,
- risk attribution,
- management reporting,
- reconciliation across existing systems.

The product is not intended to replace the firm's ETRM. It is intended to sit above existing systems as an analytical and decision-support layer.

The first real commercial engagement, if pursued, should be a narrow desk-level pilot rather than an enterprise-wide rollout.

See [ENTERPRISE_PILOT.md](ENTERPRISE_PILOT.md).

---

## 3. First business problem

The first problem is:

> A crude portfolio has physical exposure and futures hedges. The risk or analytics team wants to understand how a market move changes physical value, hedge value, remaining exposure, and which component drives the result.

A simple controlled example:

- expected production: 100,000 barrels,
- current crude price: $70 per barrel,
- scenario price: $60 per barrel,
- hedge coverage: 75%.

Before software is trusted, the result must be understandable and reproducible by hand.

---

## 4. v0.1 scope

Version 0.1 will use **controlled sample data** for a fictional crude-oil business unit.

The system will eventually read small input files representing physical exposure, hedge exposure, and a scenario.

Core fields will include items such as:

| Field | Meaning |
|---|---|
| exposure_id | Unique identifier for the physical exposure |
| business_unit | Portfolio or business-unit label |
| commodity | Commodity being analyzed |
| location | Delivery or exposure location |
| delivery_month | Period in which exposure occurs |
| volume | Physical quantity exposed |
| volume_unit | Unit of the physical quantity |
| reference_price | Starting market price |
| hedge_id | Unique identifier for a hedge |
| hedge_instrument | Instrument used for the hedge |
| contract_month | Hedge contract month |
| contracts | Number of futures contracts |
| contract_multiplier | Quantity represented by one futures contract |

The first scenario will be a simple flat-price move.

Example:

> WTI decreases by $10 per barrel.

The engine must calculate:

1. gross physical exposure,
2. hedged volume,
3. unhedged volume,
4. hedge percentage,
5. physical price impact,
6. futures hedge impact,
7. net flat-price result,
8. calculation trace.

---

## 5. v0.1 exclusions

The first version will **not** include:

- live CME/NYMEX data,
- options or Greeks,
- complex swaps,
- refinery economics,
- crack spreads,
- basis modeling,
- VaR,
- Expected Shortfall,
- EIA API integration,
- databases,
- dashboards,
- user accounts,
- AI commentary,
- live ETRM integrations,
- automated trading,
- trade recommendations.

These may be considered later only after the core exposure/scenario engine is correct.

---

## 6. Beginner mental model

The project can be understood as four boxes:

```text
Company exposure
      ↓
Hedge information
      ↓
Market scenario
      ↓
Financial impact
```

Example:

```text
100,000 barrels expected production
             ↓
75% hedged with WTI futures
             ↓
WTI falls by $10/bbl
             ↓
Physical loss + hedge gain = net result
```

The software is simply automating this logic in a controlled and repeatable way.

---

## 7. Core design rules

### Deterministic calculations

The same inputs must always produce the same outputs.

### Auditability

A result should be traceable to the inputs and assumptions used to calculate it.

### Validation before calculation

If required fields are missing, units are invalid, or values cannot be interpreted, the calculation should fail clearly instead of guessing.

### Separation of concerns

Data loading, validation, calculation, and reporting should be separate pieces of the system.

### Integration readiness

Prototype files should be modeled so that later enterprise inputs can arrive from ETRM exports, APIs, databases, or approved market-data feeds without replacing the analytical core.

### No numerical dependence on an LLM

If AI is added later, it may translate user language into structured inputs or explain results. It will not calculate official portfolio numbers.

---

## 8. v0.1 success criteria

v0.1 is complete only when:

- sample exposure and hedge data load successfully,
- invalid inputs are rejected clearly,
- hedge coverage is calculated correctly,
- one flat-price scenario is calculated correctly,
- results match a hand-calculated example,
- automated tests verify the main calculations,
- outputs are understandable without reading source code,
- every material result can be traced to its inputs and formula,
- documentation explains all assumptions.

If any of these fail, development does not advance to the next stage.

---

## 9. Long-term modules

Possible future modules include:

- Exposure Analytics
- Scenario Lab
- P&L Explain
- Hedge Analytics
- Market Intelligence
- Historical Scenario Replay
- Market-State Research
- Risk Analytics
- Monitoring and Alerts
- Reporting and API Access
- Enterprise Data / ETRM Integrations

These are roadmap directions, not promises of current functionality.
