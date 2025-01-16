##2023 yılı içinde her ürün için minimum,maksimum ve fiyat değişimleri

SELECT 
    name,
    type,
    MIN(min_price) AS min_fiyat,
    MAX(max_price) AS max_fiyat,
    (MAX(max_price) - MIN(min_price)) AS fiyat_degisimi
FROM 
    worksheet
WHERE 
    YEAR(date) = 2023  
GROUP BY 
    name, type
ORDER BY 
    fiyat_degisimi DESC;
