
SELECT 
    name,
    type,
    MIN(min_price) AS min_price,
    MAX(max_price) AS max_price,
    (MAX(max_price) - MIN(min_price)) AS price_change
FROM 
    worksheet
WHERE 
    YEAR(date) = 2022  
GROUP BY 
    name, type
ORDER BY 
    price_change DESC;