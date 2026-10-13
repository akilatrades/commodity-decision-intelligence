# Physical crude book: pricing, delivery and invoice reconciliation in SQL

Every month a physical crude desk has to answer the same questions: what did each deal price at, did the barrels actually move, are the invoices right, what flat-price risk is still open, and what did the book make? This project answers them in SQL for a small **synthetic** book of Permian and Cushing purchases sold into Houston, priced off a real WTI calendar-month average (CMA) proxy.

**What the reports find:**

- **Four invoice breaks.** A purchase invoice priced off July's CMA instead of August's ($485,431 under-billed), a wrong differential (+$0.85 instead of +$0.80, $7,508 over-billed), contract barrels billed instead of ticketed barrels (900 bbl, $86,118 over-billed), and a $14.6 million sale that was never invoiced.
- **One short delivery.** A refiner took 111,000 of 120,000 bbl, 7.5% short of a ±5% tolerance.
- **10,000 bbl of open flat-price risk.** A 60,000 bbl fixed-price September sale was hedged with only 50,000 bbl of CMA swaps. WTI's CMA rose from $82.45 in August to $95.69 in September, and the missing 10,000 bbl of swaps would have earned about $32,900.

The deals, tickets, invoices and swaps are invented; the breaks were planted on purpose ([`build_book.py`](build_book.py) lists them), and the tests check that the SQL finds exactly those and nothing else.

## The book

| Deal | Side | Location | Month | Contract bbl | Pricing |
|---|---|---|---|---:|---|
| D001 | Buy | Midland | Aug 2026 | 150,000 | CMA + 0.85 |
| D002 | Buy | Midland | Aug 2026 | 90,000 | Fixed $81.90 |
| D003 | Sell | Houston | Aug 2026 | 120,000 | CMA + 1.35 |
| D004 | Sell | Houston | Aug 2026 | 120,000 | CMA + 1.20 |
| D005 | Buy | Midland | Sep 2026 | 150,000 | CMA + 0.80 |
| D006 | Buy | Cushing | Sep 2026 | 60,000 | CMA + 0.00 |
| D007 | Sell | Houston | Sep 2026 | 150,000 | CMA + 1.40 |
| D008 | Sell | Houston | Sep 2026 | 60,000 | Fixed $93.00 |

Fixed-price deals are hedged with WTI CMA swaps that settle against the same monthly average: short 90,000 bbl at $81.60 for August, long 50,000 bbl at $92.40 for September. Barrels move to Houston at assumed tariffs of $0.55/bbl from Midland and $0.90/bbl from Cushing.

## Reports

| Query | Question it answers |
|---|---|
| [`views.sql`](sql/views.sql) | The monthly CMA, each deal's contract price, ticketed barrels and expected settlement |
| [`invoice_reconciliation.sql`](sql/invoice_reconciliation.sql) | Does each invoice match ticketed barrels at the contract price? If not, is it volume, price, both, or missing? |
| [`delivery_check.sql`](sql/delivery_check.sql) | Did each deal deliver within its tolerance? |
| [`positions.sql`](sql/positions.sql) | Net physical barrels and remaining flat-price exposure by month |
| [`pnl.sql`](sql/pnl.sql) | Sales minus purchases, transport and swap settlement, with unsold barrels marked at the CMA |

### Invoice reconciliation

| Deal | Status | Contract price | Invoiced price | Ticketed bbl | Invoiced bbl | Difference |
|---|---|---:|---:|---:|---:|---:|
| D001 | Price | 83.3024 | 80.0705 | 150,200 | 150,200 | −$485,431 |
| D005 | Price | 96.4871 | 96.5371 | 150,150 | 150,150 | +$7,508 |
| D006 | Volume | 95.6871 | 95.6871 | 59,100 | 60,000 | +$86,118 |
| D007 | Missing invoice | 97.0871 | — | 150,050 | — | −$14,567,919 |

The other four deals match to the cent. [Full reconciliation](outputs/invoice_reconciliation.csv) · [Delivery check](outputs/delivery_check.csv)

### Positions and P&L

| Month | Net physical bbl | Fixed-price bbl | Swaps bbl | Net flat-price bbl | Book P&L |
|---|---:|---:|---:|---:|---:|
| Aug 2026 | 0 | +90,000 | −90,000 | 0 | +$7,130 |
| Sep 2026 | 0 | −60,000 | +50,000 | −10,000 | −$42,693 |

P&L uses contract prices on ticketed barrels, not the invoices, so billing errors do not distort the book. August's 9,140 unsold barrels, left behind by the short delivery, are marked at the August CMA. The Midland-to-Houston CMA trades are thin or negative once the $0.55 tariff is paid: August barrels bought at CMA + 0.85 land in Houston at CMA + 1.40 and sold at CMA + 1.35 and + 1.20. [Positions](outputs/positions.csv) · [P&L](outputs/pnl.csv) · [CMA](outputs/cma.csv)

## Run it

From this directory:

```bash
pip install -r requirements.txt
pytest test_book.py
python build_book.py   # rewrites the synthetic book (deterministic)
python book.py         # loads it into SQLite and saves every report
```

## Data

The book in `data/book/` is synthetic. The CMA comes from `data/cl_front_month_proxy_2026q3.csv`: Yahoo Finance continuous front-month WTI closes for July–September 2026, copied from the saved snapshot in [energy-commodity-var-engine](https://github.com/akilatrades/energy-commodity-var-engine/tree/main/outputs/sample_run_2026-10). The proxy CMA is a simple average of those closes; the NYMEX CMA averages exchange settlements of the prompt contract and rolls at expiry. A deal month without a full month of prices fails rather than pricing off a partial average.

## What I learned / what I would do differently

The P&L should come from contract terms and tickets, and the invoices should be checked against that, not the other way round; otherwise every billing error becomes a trading result. Next I would add nominations and pipeline schedules so volume breaks can be traced to the day they happened, line loss and quality adjustments on tickets, and a pricing calendar that respects the actual CMA roll.

## Limitations

Synthetic deals, tickets, invoices and swaps; one month of tickets per deal with no daily scheduling; constant tariffs; no quality bank, line loss, credit terms, payment dates or taxes. Unsold barrels are marked at the WTI CMA rather than a Houston price.
