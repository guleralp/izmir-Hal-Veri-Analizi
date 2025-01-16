SELECT 
    name,
    date,
    min_price,
    max_price,
    avg_price
FROM worksheet

WHERE YEAR(date) = 2022
    AND name = (
        SELECT name
        FROM worksheet
        WHERE YEAR(date) = 2022
        GROUP BY name
        ORDER BY MAX(max_price) DESC
        LIMIT 1
    )
ORDER BY date;
