SELECT 
    name,
    type,
    MIN(min_price) AS min_fiyat,
     Round(AVG(avg_price),2) as avg_fiyat,
    MAX(max_price) AS max_fiyat,
    (MAX(max_price) - MIN(min_price)) AS fiyat_degisim
FROM 
    worksheet
WHERE 
    YEAR(DATE) = '2024'
GROUP BY 
    name, type
ORDER BY 
    fiyat_degisim DESC
    LIMIT 5;