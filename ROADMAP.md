# Roadmap

Development is intentionally staged. Each stage has a quality gate. A later stage should not be started merely because the previous code runs once.

## Step 0 — Product definition

**Goal:** Define the user, problem, scope, data rules, and success criteria.

Deliverables:

- README
- project specification
- data policy
- roadmap

**Gate:** The first business problem and v0.1 boundaries are clear.

**Status:** In progress

---

## Step 1 — Project skeleton

**Goal:** Create the smallest runnable Python project.

Planned items:

- Python project metadata
- source directory
- test directory
- sample-data directory
- basic continuous-integration test

**Gate:** The project installs and a trivial automated test passes.

---

## Step 2 — Controlled sample exposure

**Goal:** Represent one fictional crude-oil exposure in a simple input file.

**Gate:** The program can load the sample and display the fields without transforming them incorrectly.

---

## Step 3 — Exposure engine

**Goal:** Calculate physical volume, hedged volume, unhedged volume, and hedge percentage.

**Gate:** Python results equal manually calculated results.

---

## Step 4 — First scenario engine

**Goal:** Apply one flat-price shock to the physical exposure and hedge.

**Gate:** Physical impact, hedge impact, and net result match a hand-worked example.

---

## Step 5 — Input validation

**Goal:** Reject missing fields, invalid units, impossible percentages, duplicate records, and non-numeric values.

**Gate:** Intentionally bad test files fail for the expected reason.

---

## Step 6 — Scenario library

**Goal:** Add a small set of controlled scenarios such as:

- crude rally,
- crude selloff,
- production shortfall,
- over-hedge,
- basis scenario when basis modeling is introduced.

**Gate:** Every scenario has a documented equation and automated test.

---

## Step 7 — Public fundamental data

**Goal:** Introduce the first external data source, likely EIA, one series at a time.

**Gate:** Source metadata, units, dates, freshness, and transformations are validated.

---

## Step 8 — Futures market data

**Goal:** Introduce properly licensed or user-supplied futures data and document contract/roll methodology.

**Gate:** Data rights and futures construction methodology are understood before the data is used commercially.

---

## Step 9 — Risk analytics

Potential additions:

- scenario loss,
- Value at Risk,
- Expected Shortfall,
- risk attribution,
- limits.

---

## Step 10 — P&L explain

Potential decomposition:

- physical flat-price effect,
- futures hedge effect,
- basis effect,
- curve effect,
- volume effect,
- fees or other modeled costs.

---

## Step 11 — Market intelligence

Potential inputs:

- inventories,
- Cushing stocks,
- production,
- refinery utilization,
- futures curve,
- spreads,
- historical context.

---

## Step 12 — Historical scenario intelligence

**Goal:** Replay historical market changes against a current exposure and compare scenario outcomes.

---

## Step 13 — User interface

Build a dashboard only after the analytical engine is stable.

---

## Step 14 — AI interface

Potential uses:

- translate natural-language scenarios into structured inputs,
- explain deterministic outputs,
- summarize evidence.

AI will not be the numerical calculation engine.

---

## Step 15 — Enterprise readiness

Potential requirements:

- authentication,
- role-based access,
- audit logs,
- data lineage,
- secrets management,
- APIs,
- database,
- observability,
- security controls,
- ETRM/ERP integration,
- deployment architecture,
- licensing review.

This stage would be required before positioning the system as production enterprise software.
