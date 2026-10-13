-- Physical crude book (SQLite). Volumes in barrels, prices in USD/bbl.

DROP TABLE IF EXISTS cl_daily;
CREATE TABLE cl_daily (
    date                  TEXT PRIMARY KEY,
    cl_front_month_proxy  REAL NOT NULL
);

DROP TABLE IF EXISTS deals;
CREATE TABLE deals (
    deal_id         TEXT PRIMARY KEY,
    counterparty    TEXT NOT NULL,
    side            TEXT NOT NULL CHECK (side IN ('BUY', 'SELL')),
    location        TEXT NOT NULL,
    delivery_month  TEXT NOT NULL,                 -- YYYY-MM
    contract_bbl    INTEGER NOT NULL CHECK (contract_bbl > 0),
    pricing_type    TEXT NOT NULL CHECK (pricing_type IN ('FIXED', 'CMA')),
    fixed_price     REAL,                          -- FIXED deals only
    differential    REAL,                          -- CMA deals: price = CMA + differential
    tolerance_pct   REAL NOT NULL,                 -- allowed delivery shortfall or overage
    CHECK ((pricing_type = 'FIXED' AND fixed_price IS NOT NULL)
        OR (pricing_type = 'CMA' AND differential IS NOT NULL))
);

-- Meter tickets: what actually moved.
DROP TABLE IF EXISTS tickets;
CREATE TABLE tickets (
    ticket_id   TEXT PRIMARY KEY,
    deal_id     TEXT NOT NULL REFERENCES deals (deal_id),
    volume_bbl  INTEGER NOT NULL CHECK (volume_bbl > 0)
);

-- Invoices received for purchases and issued for sales.
DROP TABLE IF EXISTS invoices;
CREATE TABLE invoices (
    invoice_id      TEXT PRIMARY KEY,
    deal_id         TEXT NOT NULL REFERENCES deals (deal_id),
    invoiced_bbl    INTEGER NOT NULL,
    invoiced_price  REAL NOT NULL,
    amount          REAL NOT NULL
);

-- WTI CMA swaps; positive volume is long. Settle (CMA - fixed) x volume.
DROP TABLE IF EXISTS swaps;
CREATE TABLE swaps (
    swap_id         TEXT PRIMARY KEY,
    delivery_month  TEXT NOT NULL,
    volume_bbl      INTEGER NOT NULL,
    fixed_price     REAL NOT NULL
);

DROP TABLE IF EXISTS transport;
CREATE TABLE transport (
    origin          TEXT NOT NULL,
    destination     TEXT NOT NULL,
    tariff_per_bbl  REAL NOT NULL CHECK (tariff_per_bbl >= 0),
    PRIMARY KEY (origin, destination)
);
