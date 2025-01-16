
##2024 yılının kış aylarındaki en ucuz ve en pahalı meyveleri 

##en pahalı meyve 
 (
     SELECT 
      name, 
      MIN(min_price) AS min_price, 
      MAX(max_price) AS max_price, 
      AVG(avg_price) AS avg_price
  FROM worksheet
  WHERE type = 'MEYVE'
    AND YEAR(date) = 2024
    AND MONTH(date) IN (12, 1, 2)  ##Kış ayları: (Aralık, Ocak, Şubaf)
  GROUP BY name
  ORDER BY avg_price DESC
  LIMIT 1
)
UNION ALL
##en ucuz meyve
(
  SELECT 
      name, 
      MIN(min_price) AS min_price, 
      MAX(max_price) AS max_price, 
      AVG(avg_price) AS avg_price
  FROM worksheet
  WHERE type = 'MEYVE'
    AND YEAR(date) = 2024
    AND MONTH(date) IN (12, 1, 2)  
  GROUP BY name
  ORDER BY avg_price ASC
  LIMIT 1
);
