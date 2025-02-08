 SELECT 
    name, 
    MONTH(date) AS Month, 
    type, 
    Round(AVG(avg_price),2) AS avg_price
FROM worksheet
WHERE name IN ('ELMA  AMASYA','ELMA  STARKING')
  AND YEAR(date) = 2024
GROUP BY name, type, MONTH(date)
ORDER BY MONTH(date), type;
    