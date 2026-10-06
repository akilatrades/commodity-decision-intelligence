# Commodity Decision Intelligence

A research and analytics platform for commodity exposure, scenario analysis, risk attribution, and decision support.

## Status

**Step 0 — Product and enterprise-pilot definition complete**

The project is being designed around a **large-enterprise crude market-risk workflow**, while the first implementation remains intentionally small and uses controlled synthetic data.

## Initial product

The first module is a **Commodity Scenario & Exposure Lab**.

It will answer a simple business question:

> If market prices, production, or hedge assumptions change, how does the company's commodity exposure change, which component drives the result, and can the answer be audited?

The first version will use a fictional crude-oil business unit and deterministic sample data so every result can be checked manually before live market data or enterprise integrations are introduced.

## Enterprise positioning

The long-term product is intended to sit **above existing ETRM, market-data, spreadsheet, and operational systems** as an analytical and decision-support layer.

The first design target is a crude Market Risk / Supply & Trading Analytics workflow. A future commercial entry point would be a narrow desk-level proof of value rather than an enterprise-wide replacement project.

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
