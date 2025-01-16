    SELECT 
    name, 
    MONTH(date) AS ay, 
    type, 
    AVG(avg_price) AS ortalama_fiyat
FROM worksheet
WHERE name LIKE '%SARIMSAK%' AND  name NOT LIKE 'SARIMSAK  TAZE'
  AND YEAR(date) = 2024
GROUP BY name, type, MONTH(date)
ORDER BY MONTH(date), type;