SELECT 
    name, 
    MIN(min_price) AS min_price, 
    MAX(max_price) AS max_price,
    CASE 
        WHEN MIN(min_price) = (SELECT MIN(min_price) 
                               FROM worksheet 
                               WHERE type = 'SEBZE' 
                               AND YEAR(date) = 2024 AND MONTH(date) IN (12, 1, 2)) THEN 'En Ucuz'
        WHEN MAX(max_price) = (SELECT MAX(max_price) 
                               FROM worksheet 
                               WHERE type = 'SEBZE' 
                               AND YEAR(date) = 2024 AND MONTH(date) IN (12, 1, 2)) THEN 'En Pahalı'
    END AS price_category
FROM worksheet
WHERE type = 'SEBZE'
  AND YEAR(date) = 2024
  AND MONTH(date) IN (12, 1, 2)  -- Kış ayları: Aralık, Ocak, Şubat
GROUP BY name
HAVING price_category IS NOT NULL;
