(
  SELECT 
      name, 
      MIN(min_price) AS min_price, 
      MAX(max_price) AS max_price, 
      AVG(avg_price) AS avg_price
  FROM worksheet
  WHERE type = 'MEYVE'
    AND YEAR(date) = 2024
    AND MONTH(date) IN (9, 10, 11)  ## Sonbahar ayları: (Eylül, Ekim, Kasım)
  GROUP BY name
  ORDER BY avg_price DESC
  LIMIT 1
)
UNION ALL
(
  SELECT 
      name, 
      MIN(min_price) AS min_price, 
      MAX(max_price) AS max_price, 
      AVG(avg_price) AS avg_price
  FROM worksheet
  WHERE type = 'MEYVE'
    AND YEAR(date) = 2024
    AND MONTH(date) IN (9, 10, 11) 
  GROUP BY name
  ORDER BY avg_price ASC
  LIMIT 1
);
