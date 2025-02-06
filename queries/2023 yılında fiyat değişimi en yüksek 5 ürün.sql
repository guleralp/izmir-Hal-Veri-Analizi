SELECT 
    name,
    type,
    MIN(min_price) AS min_price,
     Round(AVG(avg_price),2) as avg_price,
    MAX(max_price) AS max_price,
    (MAX(max_price) - MIN(min_price)) AS price_change
FROM 
    worksheet
WHERE 
    YEAR(DATE) = '2023'
GROUP BY 
    name, type
ORDER BY 
    price_change DESC
    LIMIT 5;