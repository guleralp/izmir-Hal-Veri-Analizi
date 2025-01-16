
##2022-2024 yılları arasında her bir ürünün en düşük ve en yüksek fiyatları

SELECT 
    name,
    MIN(min_price) AS lowest_price,
    MAX(max_price) AS highest_price
FROM worksheet
GROUP BY name;