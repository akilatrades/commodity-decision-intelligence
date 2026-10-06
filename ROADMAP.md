# Roadmap

Development is intentionally staged. Each stage has a quality gate. A later stage should not be started merely because the previous code runs once.

The product is designed around an **enterprise crude market-risk workflow**, but enterprise integrations and security controls will be added only after the analytical core is proven.

## Step 0 — Product and enterprise-pilot definition

**Goal:** Define the user, business problem, pilot scope, data rules, success criteria, and enterprise design principles.

Deliverables:

- README
- project specification
- enterprise pilot definition
- data policy
- roadmap

**Gate:** The first business problem, v0.1 boundaries, enterprise user, and pilot objective are clear.

**Status:** Complete

---

## Step 1 — Project skeleton

**Goal:** Create the smallest runnable Python project.

Planned items:

- Python project metadata
- source directory
- test directory
- sample-data directory
- basic continuous-integration test

**Enterprise reason:** Establish a maintainable, testable foundation before business calculations are added.

**Gate:** The project installs and a trivial automated test passes.

**Status:** Complete

---

## Step 2 — Controlled enterprise-shaped sample data

**Status:** Next

**Goal:** Represent one fictional crude business unit with separate physical exposure and futures hedge inputs.

**Enterprise reason:** Model inputs in a form that could later be supplied by an ETRM export or controlled enterprise feed.

**Gate:** The program can load the samples and preserve identifiers, units, dates, and source fields correctly.

---

## Step 3 — Exposure engine

**Goal:** Calculate physical volume, hedged volume, unhedged volume, and hedge percentage.

**Enterprise reason:** Exposure is the base layer for scenario, risk, and P&L analysis.

**Gate:** Python results equal manually calculated results and retain calculation traceability.

---

## Step 4 — First scenario engine

**Goal:** Apply one flat-price shock to the physical exposure and futures hedge.

**Enterprise reason:** Demonstrate the first end-to-end desk workflow: inputs → scenario → attributed financial impact.

**Gate:** Physical impact, hedge impact, and net result match a hand-worked example.

---

## Step 5 — Input validation and controls

**Goal:** Reject missing fields, invalid units, impossible percentages, duplicate records, and non-numeric values.

**Enterprise reason:** A risk system must fail safely instead of producing plausible-looking numbers from bad inputs.

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

## Step 15 — Enterprise deployment controls

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
- licensing review,
- SSO,
- retention and access policies.

These controls are required before positioning the system as production enterprise software.
