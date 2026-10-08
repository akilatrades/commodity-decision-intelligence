# Research scope

Build a small WTI exposure calculator that answers: what happens to physical revenue and futures P&L when the reference price changes?

Current implementation: package health check, typed input records, deterministic CSV loaders and synthetic sample data. Calculation results have not been implemented or validated.

## First calculation

For each fictional exposure, compute physical barrels, hedged barrels, hedge fraction, and the separate physical and futures effects of a price change. Preserve input identifiers in the output so the total can be reconciled to every row. Reject inconsistent units and missing identifiers.

## Acceptance checks

- A hand-calculated unhedged case.
- A matched full hedge whose flat-price effects cancel.
- A partial hedge with a known residual.
- An overhedge flagged explicitly.
- Clear input validation and reproducible output.

Use synthetic inputs first. No customer deployment, commercial demand, time savings or validated risk result is claimed. Keep this prototype separate from the completed research in the WTI and VaR repositories.
