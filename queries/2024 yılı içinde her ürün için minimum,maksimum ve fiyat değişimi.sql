
##2024 yılı içinde her ürün için minimum,maksimum ve fiyat değişimi

SELECT 
    name,
    type,
    MIN(min_price) AS min_fiyat,
    MAX(max_price) AS max_fiyat,
    (MAX(max_price) - MIN(min_price)) AS fiyat_degisim
FROM 
    worksheet
WHERE 
    YEAR(date) = 2024  
GROUP BY 
    name, type
ORDER BY 
    fiyat_degisim DESC;
