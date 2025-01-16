
##Her ürün için 2022-2024 yılları arasındaki minimum ve maksimum fiyat değişimi

SELECT 
    name,
    type,
    MIN(min_price) AS min_fiyat,
    MAX(max_price) AS max_fiyat,
    (MAX(max_price) - MIN(min_price)) AS fiyat_degisim
FROM 
    worksheet
WHERE 
    date BETWEEN '2022-01-01' AND '2024-12-31'
GROUP BY 
    name, type
ORDER BY 
    fiyat_degisim DESC;