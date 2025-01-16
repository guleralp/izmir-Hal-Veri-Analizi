-- Her ürün için en düşük ve en yüksek fiyatları ve aralarındaki gün farkını hesaplamak (fiyat artış hızını hesaplamak)
SELECT 
    name,
    MIN(avg_price) AS min_price,
    MAX(avg_price) AS max_price,
    DATEDIFF(MAX(date), MIN(date)) AS days_between,
    (MAX(avg_price) - MIN(avg_price)) / DATEDIFF(MAX(date), MIN(date)) AS price_increase_rate
FROM 
    worksheet
WHERE 
    YEAR(date) = 2024
GROUP BY 
    name
ORDER BY 
    price_increase_rate DESC
LIMIT 10;