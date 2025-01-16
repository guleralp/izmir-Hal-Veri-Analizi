##2023 yılı içerisinde en yüksek fiyata sahip SEBZE

SELECT NAME, MAX(max_price) AS highest_price
FROM worksheet
WHERE YEAR(date) = 2023 AND type = 'SEBZE'
GROUP BY NAME
ORDER BY highest_price DESC
LIMIT 1;