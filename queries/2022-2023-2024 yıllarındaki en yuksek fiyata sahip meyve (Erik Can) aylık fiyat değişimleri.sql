 SELECT
    YEAR(date) AS year, MONTH(date) AS month,
    ROUND(MIN(min_price), 2) AS min_price,
    ROUND(MAX(max_price), 2) AS max_price,
    ROUND(AVG(avg_price), 2) AS avg_price
FROM worksheet
WHERE name = 'ERİK  CAN' AND YEAR(date) IN (2022, 2023, 2024)
GROUP BY year, month
ORDER BY year, month;