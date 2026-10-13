-- Did each deal deliver within its contract tolerance?

SELECT
    d.deal_id,
    d.counterparty,
    d.side,
    d.delivery_month,
    d.contract_bbl,
    v.delivered_bbl,
    v.delivered_bbl - d.contract_bbl AS difference_bbl,
    ROUND(100.0 * (v.delivered_bbl - d.contract_bbl) / d.contract_bbl, 2) AS difference_pct,
    d.tolerance_pct,
    CASE
        WHEN v.delivered_bbl < d.contract_bbl * (1 - d.tolerance_pct / 100.0) THEN 'UNDER_DELIVERED'
        WHEN v.delivered_bbl > d.contract_bbl * (1 + d.tolerance_pct / 100.0) THEN 'OVER_DELIVERED'
        ELSE 'WITHIN_TOLERANCE'
    END AS status
FROM deals AS d
JOIN delivered AS v ON v.deal_id = d.deal_id
ORDER BY d.delivery_month, d.deal_id;
