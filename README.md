# Petchem feedstock margins

How much of a polyethylene producer's margin can a feedstock hedge protect?

The [petchem feedstock project](projects/petchem-feedstock) follows public ethane and propane benchmarks through an explicit ethylene-to-PE mass balance. In the 13-quarter historical sample, the ethane-route domestic LDPE contribution proxy rises from **33.5 cents/lb in 2019 to 61.2 cents/lb in 2021–2022Q1**, despite more expensive ethane. A feedstock hedge controls one input risk; it leaves product prices and basis exposed.

The 2021 expansion coincides with product-supply disruption and recovering demand. The project connects the price data to Winter Storm Uri and lingering hurricane-related inventory shortages, then separates feedstock protection from remaining product-price exposure.

- [Model and findings](projects/petchem-feedstock/README.md)
- [Assumptions and limitations](projects/petchem-feedstock/README.md#limitations)
- [Public source provenance](projects/petchem-feedstock/SOURCES.md)
- [Saved chart and results](projects/petchem-feedstock/outputs)

## Earlier exposure prototype

The `src/commodity_decision_intelligence` package remains a separate early prototype: typed inputs, deterministic CSV loaders and synthetic WTI sample data. It does not yet perform a complete physical-exposure calculation. Its tests check ingestion and package health.

```bash
pip install -e ".[dev]"
python -m pytest
python -m commodity_decision_intelligence
```

The petchem project's reproduction instructions and dependencies are in its own directory.

## What I learned / what I would do differently

Making the mass balance explicit matters more than adding a dashboard: feedstock and polymer prices cannot be subtracted one-for-one when their quantities differ. A correct input hedge still leaves a business exposed to its product price. The next improvement is a defensible coproduct slate and independently sourced process-cost ranges, followed by a longer price history.

## License

Original code is available under the [MIT License](LICENSE). Public benchmark sources and data provenance are documented in [source notes](projects/petchem-feedstock/SOURCES.md).
