-- Position by delivery month on contract volumes.
-- CMA-priced deals float with the index, so only fixed-price deals and swaps
-- carry flat-price exposure. Positive exposure gains when WTI rises.

WITH physical AS (
    SELECT
        delivery_month,
        SUM(CASE WHEN side = 'BUY' THEN contract_bbl ELSE 0 END) AS bought_bbl,
        SUM(CASE WHEN side = 'SELL' THEN contract_bbl ELSE 0 END) AS sold_bbl,
        SUM(CASE WHEN pricing_type = 'FIXED' AND side = 'BUY' THEN contract_bbl
                 WHEN pricing_type = 'FIXED' AND side = 'SELL' THEN -contract_bbl
                 ELSE 0 END) AS fixed_price_bbl
    FROM deals
    GROUP BY delivery_month
),
hedges AS (
    SELECT delivery_month, SUM(volume_bbl) AS swap_bbl
    FROM swaps
    GROUP BY delivery_month
)
SELECT
    p.delivery_month,
    p.bought_bbl,
    p.sold_bbl,
    p.bought_bbl - p.sold_bbl AS net_physical_bbl,
    p.fixed_price_bbl,
    COALESCE(h.swap_bbl, 0) AS swap_bbl,
    p.fixed_price_bbl + COALESCE(h.swap_bbl, 0) AS net_flat_price_bbl
FROM physical AS p
LEFT JOIN hedges AS h ON h.delivery_month = p.delivery_month
ORDER BY p.delivery_month;
