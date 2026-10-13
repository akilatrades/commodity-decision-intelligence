-- Match every deal's expected settlement to its invoice and explain each break.
-- A volume break is more than 0.1% off the ticketed barrels; a price break is
-- more than $0.0005/bbl off the contract price.

SELECT
    e.deal_id,
    e.counterparty,
    e.side,
    e.delivery_month,
    e.delivered_bbl,
    i.invoiced_bbl,
    e.contract_price,
    i.invoiced_price,
    e.expected_amount,
    i.amount AS invoiced_amount,
    ROUND(COALESCE(i.amount, 0) - e.expected_amount, 2) AS amount_difference,
    CASE
        WHEN i.invoice_id IS NULL THEN 'MISSING_INVOICE'
        WHEN ABS(i.invoiced_bbl - e.delivered_bbl) > 0.001 * e.delivered_bbl
         AND ABS(i.invoiced_price - e.contract_price) > 0.0005 THEN 'VOLUME_AND_PRICE'
        WHEN ABS(i.invoiced_bbl - e.delivered_bbl) > 0.001 * e.delivered_bbl THEN 'VOLUME'
        WHEN ABS(i.invoiced_price - e.contract_price) > 0.0005 THEN 'PRICE'
        WHEN ABS(i.amount - e.expected_amount) > 1.00 THEN 'AMOUNT'
        ELSE 'MATCHED'
    END AS status
FROM expected_settlement AS e
LEFT JOIN invoices AS i ON i.deal_id = e.deal_id
ORDER BY e.delivery_month, e.deal_id;
