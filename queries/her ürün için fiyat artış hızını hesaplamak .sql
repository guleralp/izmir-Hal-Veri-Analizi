SELECT 
    name,
    MIN(avg_price) AS min_price,
    MAX(avg_price) AS max_price,
    DATEDIFF(MAX(date), MIN(date)) AS days_between,
    CASE 
        WHEN DATEDIFF(MAX(date), MIN(date)) > 0 THEN (MAX(avg_price) - MIN(avg_price)) / DATEDIFF(MAX(date), MIN(date))
        ELSE 0
    END AS price_increase_rate
FROM 
    worksheet
WHERE 
    YEAR(date) = 2024
GROUP BY 
    name
ORDER BY 
    price_increase_rate DESC;
