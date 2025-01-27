SELECT 
    name, 
    MAX(max_price) AS highest_price, 'SEBZE' AS category
FROM worksheet
WHERE YEAR(date) IN (2022, 2023, 2024)  
  AND type = 'SEBZE'  
GROUP BY name  
ORDER BY highest_price DESC  
LIMIT 1;  
