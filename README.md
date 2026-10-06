# Commodity Decision Intelligence

A research and analytics platform for commodity exposure, scenario analysis, risk attribution, and decision support.

## Status

**Step 0 — Product definition**

No production analytics have been built yet. The first implementation will focus on a small crude-oil scenario and exposure workflow using controlled sample data.

## Initial product

The first module is a **Commodity Scenario & Exposure Lab**.

It will answer a simple business question:

> If market prices, production, basis, or hedge assumptions change, how does the company's commodity exposure change?

The first version will use a fictional crude-oil producer and deterministic sample data so every result can be checked manually before live market data is introduced.

## Design principles

- Numerical results must be deterministic and testable.
- Every important input should be traceable to its source.
- Bad or incomplete inputs should be flagged instead of silently accepted.
- Public, licensed, and customer-proprietary data must remain clearly separated.
- AI may help interpret results later, but it will not be the source of numerical truth.
- New capabilities are added only after the previous layer passes validation.

## Current documents

- [PROJECT_SPEC.md](PROJECT_SPEC.md) — product purpose, users, scope, and v0.1 definition
- [DATA_POLICY.md](DATA_POLICY.md) — rules for synthetic, public, licensed, and customer data
- [ROADMAP.md](ROADMAP.md) — staged development plan and quality gates

## Long-term direction

The long-term platform may include exposure analytics, scenario analysis, P&L explain, market intelligence, hedge analytics, historical scenario replay, risk monitoring, reporting, and enterprise integrations.

Those capabilities are intentionally outside the first build.

## Disclaimer

This repository is currently a research and software-development project. It is not a trading recommendation, brokerage service, ETRM replacement, or production risk system.
