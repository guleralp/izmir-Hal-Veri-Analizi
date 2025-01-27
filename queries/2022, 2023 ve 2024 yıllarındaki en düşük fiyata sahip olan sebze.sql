SELECT name, MIN(avg_price) AS lowest_price, 'SEBZE' AS category
FROM worksheet
WHERE YEAR(date) IN (2022, 2023, 2024) AND type = 'SEBZE'
GROUP BY name
ORDER BY lowest_price ASC
LIMIT 1;