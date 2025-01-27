SELECT 
    name,
    MIN(min_price) AS lowest_price,
    MAX(max_price) AS highest_price
FROM worksheet
GROUP BY name;