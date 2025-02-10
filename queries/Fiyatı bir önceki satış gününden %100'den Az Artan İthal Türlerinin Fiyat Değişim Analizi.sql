WITH price_changes AS (
    SELECT name AS product_name, DATE, avg_price AS current_price,
           LEAD(DATE) OVER (PARTITION BY name ORDER BY DATE) AS next_date,
           LEAD(avg_price) OVER (PARTITION BY name ORDER BY DATE) AS next_price
    FROM worksheet
    WHERE type = 'İTHAL' AND YEAR(DATE) = 2024
),
max_changes AS (
    SELECT 
        product_name,
        DATE,
        current_price,
        next_price,
        ((next_price - current_price) / current_price) * 100 as price_change_pct,
        ROW_NUMBER() OVER (PARTITION BY product_name ORDER BY ((next_price - current_price) / current_price) * 100 DESC) as rn
    FROM price_changes
    WHERE next_price IS NOT NULL
    AND DATEDIFF(next_date, DATE) < 10
    AND ((next_price - current_price) / current_price) * 100 < 100
    AND ((next_price - current_price) / current_price) * 100 > 0
)
SELECT 
    product_name, 
    DATE_FORMAT(DATE, '%Y-%m-%d') AS "change_date",
    ROUND(current_price, 2) AS "current_price",
    ROUND(next_price, 2) AS "next_price",
    ROUND(price_change_pct, 2) AS "price_change (%)"
FROM max_changes
WHERE rn = 1
ORDER BY `price_change (%)` DESC;