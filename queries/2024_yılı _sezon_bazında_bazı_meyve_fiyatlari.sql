SELECT name,
       season,
       Round(AVG(CASE WHEN YEAR(date) = 2024 THEN avg_price END),2) AS avg_price_2024
FROM (
    SELECT *,
           CASE 
               WHEN MONTH(date) IN (3, 4, 5) THEN 'İlkbahar'
               WHEN MONTH(date) IN (6, 7, 8) THEN 'Yaz'
               WHEN MONTH(date) IN (9, 10, 11) THEN 'Sonbahar'
               ELSE 'Kış'
           END AS season
    FROM worksheet
    WHERE name IN (
          'ELMA  AMASYA', 'ARMUT  DEVECI', 'Mandalina', 
        'Portakal','Karpuz', 
         'KAVUN  SERA', 'Kayısı', 'Muz',
        'ÜZÜM  BEYAZ'
    )
) AS seasonal_data
GROUP BY name, season
ORDER BY name, season;