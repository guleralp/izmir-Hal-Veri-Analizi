##2024 yılı içindeki en yüksek fiyat 

SELECT name, MAX(max_price) AS highest_price
FROM worksheet
WHERE YEAR(date) = 2024
GROUP BY name
ORDER BY highest_price DESC
LIMIT 1;

