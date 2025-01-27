SELECT name, MIN(avg_price) AS lowest_price, 'MEYVE' AS category
FROM worksheet
WHERE YEAR(date) IN (2022, 2023, 2024) AND type = 'MEYVE'
GROUP BY name
ORDER BY lowest_price ASC
LIMIT 1;