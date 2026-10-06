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

The first goal is much smaller.

---

## 2. Initial customer

The first target user is a **small or mid-sized commodity business or trading team** that has real commodity exposure but does not have a large internal quantitative engineering team.

Examples could eventually include:

- producers,
- commodity marketers,
- fuel distributors,
- refiners,
- petrochemical companies,
- small trading firms,
- commercial or risk teams.

Large enterprise customers are a long-term target, not the starting implementation target.

---

## 3. First business problem

The first problem is:

> A company has physical crude-oil exposure and futures hedges. It wants to understand how a market move changes its physical value, hedge value, and remaining exposure.

A simple example:

- expected production: 100,000 barrels,
- current crude price: $70 per barrel,
- scenario price: $60 per barrel,
- hedge coverage: 75%.

Before software is trusted, the result must be understandable and reproducible by hand.

---

## 4. v0.1 scope

Version 0.1 will use **controlled sample data** for a fictional crude-oil producer.

The system will eventually read a small input file containing fields such as:

| Field | Meaning |
|---|---|
| exposure_id | Unique identifier for the exposure |
| commodity | Commodity being analyzed |
| volume | Physical quantity exposed |
| volume_unit | Unit of the physical quantity |
| reference_price | Starting market price |
| hedge_ratio | Percentage of exposure hedged |
| hedge_instrument | Instrument used for the hedge |
| contract_multiplier | Quantity represented by one futures contract |

The first scenario will be a simple flat-price move.

Example:

> WTI decreases by $10 per barrel.

The engine must calculate:

1. physical price impact,
2. futures hedge impact,
3. net flat-price result,
4. hedged volume,
5. unhedged volume,
6. hedge percentage.

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
- ETRM integrations,
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

### No numerical dependence on an LLM

If AI is added later, it may translate user language into structured inputs or explain results. It will not calculate official portfolio numbers.

---

## 8. v0.1 success criteria

v0.1 is complete only when:

- sample exposure data loads successfully,
- invalid inputs are rejected clearly,
- hedge coverage is calculated correctly,
- one flat-price scenario is calculated correctly,
- results match a hand-calculated example,
- automated tests verify the main calculations,
- outputs are understandable without reading source code,
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
