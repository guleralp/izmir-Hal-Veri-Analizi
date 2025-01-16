
SELECT 
    name,
    date,
    min_price,
    max_price,
    avg_price
FROM worksheet

WHERE YEAR(date) = 2023
    AND name = (
        SELECT name
        FROM worksheet
        WHERE YEAR(date) = 2023
        GROUP BY name
        ORDER BY MIN(min_price) ASC
        LIMIT 1
    )
ORDER BY date;
