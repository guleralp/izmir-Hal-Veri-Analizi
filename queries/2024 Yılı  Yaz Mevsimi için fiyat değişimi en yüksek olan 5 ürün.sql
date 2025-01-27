SELECT 
    name, 
    type,
    ROUND(MAX(CASE WHEN MONTH(date) IN (6, 7, 8) AND YEAR(date) = 2024 THEN avg_price END), 2) AS max_price,
    ROUND(MIN(CASE WHEN MONTH(date) IN (6, 7, 8) AND YEAR(date) = 2024 THEN avg_price END), 2) AS min_price,
    ROUND(MAX(CASE WHEN MONTH(date) IN (6, 7, 8) AND YEAR(date) = 2024 THEN avg_price END) - 
          MIN(CASE WHEN MONTH(date) IN (6, 7, 8) AND YEAR(date) = 2024 THEN avg_price END), 2) AS price_change
FROM worksheet
WHERE YEAR(date) = 2024
GROUP BY name, type
ORDER BY price_change DESC
LIMIT 5;
