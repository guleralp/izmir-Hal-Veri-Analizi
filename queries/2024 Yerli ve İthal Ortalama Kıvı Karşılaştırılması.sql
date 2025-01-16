        SELECT 
    name, 
    MONTH(date) AS ay, 
    type, 
    Round(AVG(avg_price),2) AS ortalama_fiyat
FROM worksheet
WHERE name LIKE 'KIVI%' 
  AND YEAR(date) = 2024
GROUP BY name, type, MONTH(date)
ORDER BY MONTH(date), type;