##2023 yılı içerisinde en yüksek fiyata sahip MEYVE

SELECT name, MAX(max_price) AS highest_price
FROM worksheet
WHERE YEAR(date) = 2023 AND type = 'MEYVE'
GROUP BY name
ORDER BY highest_price DESC
LIMIT 1;