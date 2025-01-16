
##2024 yılının yaz aylarındaki en ucuz ve en pahalı meyveler


SELECT 
    name, 
    MIN(min_price) AS min_price, 
    MAX(max_price) AS max_price, 
    AVG(avg_price) AS avg_price,
    CASE 
        WHEN MIN(min_price) = 
        (SELECT MIN(min_price) FROM worksheet 
        WHERE type = 'MEYVE' 
        AND YEAR(date) = 2024 AND MONTH(date) IN (6, 7, 8)) THEN 'En Ucuz'
        
        WHEN MAX(max_price) = 
        (SELECT MAX(max_price) FROM worksheet 
        WHERE type = 'MEYVE' 
        AND YEAR(date) = 2024 AND MONTH(date) IN (6, 7, 8)) THEN 'En Pahalı'
    END AS price_category
FROM worksheet
WHERE type = 'MEYVE'
  AND YEAR(date) = 2024
  AND MONTH(date) IN (6, 7, 8)  -- Yaz ayları: Haziran, Temmuz, Ağustos
GROUP BY name
HAVING price_category IS NOT NULL;
