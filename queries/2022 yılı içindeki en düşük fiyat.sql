##2022 yılı içindeki en düşük fiyat

SELECT 
    name, 
    MIN(min_price) AS lowest_price
FROM worksheet
WHERE YEAR(date) = 2022
GROUP BY name
ORDER BY lowest_price ASC
LIMIT 1;