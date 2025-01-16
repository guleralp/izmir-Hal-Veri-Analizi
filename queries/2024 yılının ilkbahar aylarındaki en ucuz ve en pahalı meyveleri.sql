(
  SELECT 
      name, 
      MIN(min_price) AS min_price, 
      MAX(max_price) AS max_price, 
      AVG(avg_price) AS avg_price
  FROM worksheet
  WHERE type = 'MEYVE'
    AND YEAR(date) = 2024
    AND MONTH(date) IN (3, 4, 5) ## İlkbahar ayları: (Mart, Nisan, Mayıs)
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
    AND MONTH(date) IN (3, 4, 5) 
  GROUP BY name
  ORDER BY avg_price ASC
  LIMIT 1
);
