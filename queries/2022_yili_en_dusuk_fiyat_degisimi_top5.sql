WITH price_changes AS (
    SELECT 
        name,
        MIN(min_price) as min_price,
        MAX(max_price) as max_price,
        AVG(avg_price) as avg_price,
        MAX(max_price) - MIN(min_price) as price_change
    FROM worksheet
    WHERE YEAR(date) = 2022
    GROUP BY name
)
SELECT *
FROM price_changes
ORDER BY price_change ASC
LIMIT 5; 