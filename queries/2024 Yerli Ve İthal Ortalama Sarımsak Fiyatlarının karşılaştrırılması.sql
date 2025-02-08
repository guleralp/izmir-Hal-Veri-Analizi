  SELECT 
    name, 
    MONTH(date) AS Month, 
    type, 
    AVG(avg_price) AS avg_price
FROM worksheet

WHERE name LIKE '%SARIMSAK%' AND  name NOT LIKE 'SARIMSAK  TAZE'
  AND YEAR(date) = 2024
GROUP BY name, type, MONTH(date)
ORDER BY MONTH(date), type;