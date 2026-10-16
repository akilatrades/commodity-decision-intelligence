# Commodity decision intelligence

Two projects on the physical side of commodity markets, built to answer one question each with public data and SQL or Python a desk analyst could check.

## Petchem feedstock margins

How much of a polyethylene producer's margin can a feedstock hedge protect?

**Less than it looks.** The [petchem feedstock project](projects/petchem-feedstock) follows public ethane and propane prices through an explicit mass balance (feedstock to ethylene to polyethylene), so the input and the product are compared in the same units. Over 13 quarters (2019 to early 2022) the ethane-route LDPE margin proxy rose from **33.5 cents/lb in 2019 to 61.2 cents/lb in 2021 to 2022Q1** even though ethane got more expensive: the product price did the work. A feedstock hedge fixes one input cost and leaves the product price, which moved more, fully exposed.

The 2021 jump lines up with Winter Storm Uri and hurricane-related supply outages tightening product supply while demand recovered.

- [Model and findings](projects/petchem-feedstock/README.md)
- [Assumptions and limitations](projects/petchem-feedstock/README.md#limitations)
- [Public source provenance](projects/petchem-feedstock/SOURCES.md)
- [Saved chart and results](projects/petchem-feedstock/outputs)

## Physical crude book

Can SQL do a crude desk's month-end? The [physical crude book](projects/physical-crude-book) builds a synthetic book of Permian and Cushing purchases sold into Houston, priced off a WTI calendar-month-average proxy built from real prices, and runs the month-end in SQL: deal pricing, delivery checks against tickets, invoice reconciliation, flat-price position and P&L. I planted four invoice errors and one short delivery; the reconciliation finds all five, and the position report shows 10,000 barrels of a fixed-price sale left unhedged.

- [Reports and findings](projects/physical-crude-book/README.md)
- [SQL queries](projects/physical-crude-book/sql)

## Earlier exposure prototype

The `src/commodity_decision_intelligence` package is an earlier prototype: typed inputs, CSV loaders and synthetic WTI sample data. It does not yet do a full physical-exposure calculation; its tests cover ingestion and package health.

```bash
pip install -e ".[dev]"
python -m pytest
python -m commodity_decision_intelligence
```

The petchem project's reproduction instructions and dependencies are in its own directory.

## What I learned / what I would do differently

Writing the mass balance down mattered more than any chart: you cannot subtract a feedstock price from a polymer price when a pound of one does not make a pound of the other. And a hedge that is correct for its input still leaves the business exposed to its product. Next I would add a defensible coproduct slate and independently sourced process-cost ranges, then a longer price history.

## License

Original code is available under the [MIT License](LICENSE). Public benchmark sources and data provenance are documented in [source notes](projects/petchem-feedstock/SOURCES.md).
