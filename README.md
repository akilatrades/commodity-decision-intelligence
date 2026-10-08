# Commodity exposure prototype

If a producer changes its production forecast or futures hedge, how does its exposure change?

This repository does not answer that question yet. It currently has typed inputs, deterministic CSV loaders, a small synthetic WTI dataset and tests. The exposure calculations are still to be built. It is an early research prototype.

## Current scope

The sample represents fictional physical exposure, futures positions and a price scenario. No client data, live positions or measured business results are included.

```bash
python -m pip install -e ".[dev]"
python -m commodity_decision_intelligence
python -m pytest
```

Passing tests currently verify package health and sample-data ingestion, not a complete risk calculation.

## What I learned / what I would do differently

A working loader is useful groundwork, but it is not an analytical finding. I would complete one hand-checkable exposure calculation before expanding the product description. The next gate is to reconcile physical P&L plus futures P&L to a manually calculated example, including the case of a full hedge.

[Research scope](PROJECT_SPEC.md) · [Next steps](ROADMAP.md) · [Data policy](DATA_POLICY.md)
