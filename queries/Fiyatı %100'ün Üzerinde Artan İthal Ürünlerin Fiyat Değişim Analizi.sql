WITH price_changes AS (
    SELECT name AS product_name, DATE, avg_price AS current_price,
           LEAD(DATE) OVER (PARTITION BY name ORDER BY DATE) AS next_date,
           LEAD(avg_price) OVER (PARTITION BY name ORDER BY DATE) AS next_price
    FROM worksheet
    WHERE type = 'İTHAL' 
)
SELECT product_name, DATE_FORMAT(DATE, '%Y-%m-%d') AS "change_date", 
       ROUND(current_price, 2) AS "current_price", ROUND(next_price, 2) AS "next_price",
       ROUND(((next_price - current_price) / current_price) * 100, 2) AS "price_change (%)"
FROM price_changes
WHERE next_price IS NOT NULL
  AND DATEDIFF(next_date, DATE) < 10  
  AND ((next_price - current_price) / current_price) * 100 > 50 
ORDER BY product_name, DATE;
