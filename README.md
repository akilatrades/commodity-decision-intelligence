# Commodity Decision Intelligence

A research and analytics platform for commodity exposure, scenario analysis, risk attribution, and decision support.

## Status

**Step 2 — Controlled enterprise-shaped sample data complete**

The project is being designed around a **large-enterprise crude market-risk workflow**, while the first implementation remains intentionally small and uses controlled synthetic data.

The repository now contains a runnable Python package, automated tests, GitHub Actions continuous integration, typed input models, deterministic CSV loaders, and a controlled synthetic WTI dataset representing physical exposure, futures hedges, and a market scenario. Commodity exposure calculations have **not** been added yet.

**Next:** Step 3 — exposure engine.

## Initial product

The first module is a **Commodity Scenario & Exposure Lab**.

It will answer a simple business question:

> If market prices, production, or hedge assumptions change, how does the company's commodity exposure change, which component drives the result, and can the answer be audited?

The first version will use a fictional crude-oil business unit and deterministic sample data so every result can be checked manually before live market data or enterprise integrations are introduced.

## Enterprise positioning

The long-term product is intended to sit **above existing ETRM, market-data, spreadsheet, and operational systems** as an analytical and decision-support layer.

The first design target is a crude Market Risk / Supply & Trading Analytics workflow. A future commercial entry point would be a narrow desk-level proof of value rather than an enterprise-wide replacement project.

## Current repository structure

```text
commodity-decision-intelligence/
├── .github/workflows/          # Automated tests
├── data/sample/                # Synthetic physical, hedge, and scenario inputs
├── src/
│   └── commodity_decision_intelligence/
│       ├── __init__.py
│       ├── __main__.py
├── tests/                      # Automated Python tests
├── DATA_POLICY.md
├── ENTERPRISE_PILOT.md
├── PROJECT_SPEC.md
├── ROADMAP.md
└── pyproject.toml
```

## Run the project locally

### 1. Install Python

Use Python 3.11 or newer.

Check your installed version:

```bash
python --version
```

On some systems the command is:

```bash
python3 --version
```

### 2. Create a virtual environment

From the repository folder:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install the project and test tools

```bash
python -m pip install -e ".[dev]"
```

### 4. Run the package

```bash
python -m commodity_decision_intelligence
```

Expected output:

```text
commodity-decision-intelligence | status=ok | stage=step-1-project-skeleton
```

### 5. Run the automated tests

```bash
python -m pytest
```

A passing test run confirms that the basic project skeleton is working.

## Design principles

- Numerical results must be deterministic and testable.
- Every important input and output should be traceable.
- Bad or incomplete inputs should be flagged instead of silently accepted.
- Public, licensed, and customer-proprietary data must remain clearly separated.
- Prototype data structures should be integration-ready.
- AI may help interpret results later, but it will not be the source of numerical truth.
- New capabilities are added only after the previous layer passes validation.

## Current documents

- [PROJECT_SPEC.md](PROJECT_SPEC.md) — product purpose, enterprise user, scope, and v0.1 definition
- [ENTERPRISE_PILOT.md](ENTERPRISE_PILOT.md) — first enterprise workflow, pilot scope, outputs, and success criteria
- [DATA_POLICY.md](DATA_POLICY.md) — rules for synthetic, public, licensed, and customer data
- [ROADMAP.md](ROADMAP.md) — staged development plan and quality gates

## Long-term direction

The long-term platform may include exposure analytics, scenario analysis, P&L explain, market intelligence, hedge analytics, historical scenario replay, risk monitoring, reporting, and enterprise integrations.

Those capabilities are intentionally outside the first build.

## Disclaimer

This repository is currently a research and software-development project. It is not a trading recommendation, brokerage service, ETRM replacement, or production risk system.
