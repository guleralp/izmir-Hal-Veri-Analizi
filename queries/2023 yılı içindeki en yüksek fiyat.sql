##2023 yılı içindeki en yüksek fiyat 

SELECT name, MAX(max_price) AS highest_price
FROM worksheet
WHERE YEAR(date) = 2023
GROUP BY name
ORDER BY highest_price DESC
LIMIT 1;
