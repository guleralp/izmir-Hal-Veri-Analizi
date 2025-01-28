SELECT 
    name, type,
    ROUND(MAX(CASE WHEN MONTH(date) IN (9, 10, 11) AND YEAR(date) = 2023 THEN avg_price END), 2) AS max_price,
    ROUND(MIN(CASE WHEN MONTH(date) IN (9, 10, 11) AND YEAR(date) = 2023 THEN avg_price END), 2) AS min_price,
    ROUND(MAX(CASE WHEN MONTH(date) IN (9, 10, 11) AND YEAR(date) = 2023 THEN avg_price END) - 
          MIN(CASE WHEN MONTH(date) IN (9, 10, 11) AND YEAR(date) = 2023 THEN avg_price END), 2) AS price_change
FROM worksheet
WHERE YEAR(date) = 2023
GROUP BY name, type
ORDER BY price_change DESC
LIMIT 5;
