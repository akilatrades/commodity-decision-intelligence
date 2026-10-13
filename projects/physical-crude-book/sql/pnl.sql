-- Monthly book P&L on delivered barrels, in USD.
-- Sales revenue - purchase cost - transport to Houston + swap settlement,
-- with any barrels bought but not sold marked at the month's CMA.

WITH flows AS (
    SELECT
        e.delivery_month,
        SUM(CASE WHEN e.side = 'SELL' THEN e.expected_amount ELSE 0 END) AS sales_revenue,
        SUM(CASE WHEN e.side = 'BUY' THEN e.expected_amount ELSE 0 END) AS purchase_cost,
        SUM(CASE WHEN e.side = 'BUY' THEN e.delivered_bbl * t.tariff_per_bbl ELSE 0 END)
            AS transport_cost,
        SUM(CASE WHEN e.side = 'BUY' THEN e.delivered_bbl ELSE -e.delivered_bbl END)
            AS unsold_bbl
    FROM expected_settlement AS e
    LEFT JOIN transport AS t
        ON t.origin = e.location AND t.destination = 'Houston'
    GROUP BY e.delivery_month
),
swap_settlement AS (
    SELECT s.delivery_month, SUM((c.cma - s.fixed_price) * s.volume_bbl) AS swap_pnl
    FROM swaps AS s
    JOIN cma AS c ON c.month = s.delivery_month
    GROUP BY s.delivery_month
)
SELECT
    f.delivery_month,
    ROUND(f.sales_revenue, 2) AS sales_revenue,
    ROUND(f.purchase_cost, 2) AS purchase_cost,
    ROUND(f.transport_cost, 2) AS transport_cost,
    ROUND(COALESCE(s.swap_pnl, 0), 2) AS swap_pnl,
    f.unsold_bbl,
    ROUND(f.unsold_bbl * c.cma, 2) AS unsold_inventory_value,
    ROUND(f.sales_revenue - f.purchase_cost - f.transport_cost
          + COALESCE(s.swap_pnl, 0) + f.unsold_bbl * c.cma, 2) AS book_pnl
FROM flows AS f
JOIN cma AS c ON c.month = f.delivery_month
LEFT JOIN swap_settlement AS s ON s.delivery_month = f.delivery_month
ORDER BY f.delivery_month;
