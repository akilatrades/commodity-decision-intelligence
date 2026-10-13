-- Monthly WTI CMA proxy: the average of front-month closes over the month's
-- trading days. The real NYMEX CMA uses exchange settlements and rolls at expiry.
DROP VIEW IF EXISTS cma;
CREATE VIEW cma AS
SELECT
    substr(date, 1, 7) AS month,
    ROUND(AVG(cl_front_month_proxy), 4) AS cma,
    COUNT(*) AS trading_days
FROM cl_daily
GROUP BY substr(date, 1, 7);

-- What each deal should price at under its contract terms.
DROP VIEW IF EXISTS deal_prices;
CREATE VIEW deal_prices AS
SELECT
    d.*,
    c.cma,
    CASE d.pricing_type
        WHEN 'FIXED' THEN d.fixed_price
        ELSE ROUND(c.cma + d.differential, 4)
    END AS contract_price
FROM deals AS d
LEFT JOIN cma AS c ON c.month = d.delivery_month;

-- Barrels that actually moved, from meter tickets.
DROP VIEW IF EXISTS delivered;
CREATE VIEW delivered AS
SELECT
    d.deal_id,
    COALESCE(SUM(t.volume_bbl), 0) AS delivered_bbl,
    COUNT(t.ticket_id) AS ticket_count
FROM deals AS d
LEFT JOIN tickets AS t ON t.deal_id = d.deal_id
GROUP BY d.deal_id;

-- Expected settlement: delivered barrels at the contract price.
DROP VIEW IF EXISTS expected_settlement;
CREATE VIEW expected_settlement AS
SELECT
    p.deal_id,
    p.counterparty,
    p.side,
    p.location,
    p.delivery_month,
    p.contract_bbl,
    v.delivered_bbl,
    p.contract_price,
    ROUND(v.delivered_bbl * p.contract_price, 2) AS expected_amount
FROM deal_prices AS p
JOIN delivered AS v ON v.deal_id = p.deal_id;
