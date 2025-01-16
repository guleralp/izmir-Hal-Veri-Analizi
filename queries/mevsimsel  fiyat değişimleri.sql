
SELECT 
    name,
    ROUND(COALESCE(AVG(CASE WHEN MONTH(date) IN (3, 4, 5) THEN avg_price END), 0), 2) AS ilkbahar_avg_price,
    ROUND(COALESCE(AVG(CASE WHEN MONTH(date) IN (6, 7, 8) THEN avg_price END), 0), 2) AS yaz_avg_price,
    ROUND(COALESCE(AVG(CASE WHEN MONTH(date) IN (9, 10, 11) THEN avg_price END), 0), 2) AS sonbahar_avg_price,
    ROUND(COALESCE(AVG(CASE WHEN MONTH(date) IN (12, 1, 2) THEN avg_price END), 0), 2) AS kış_avg_price
FROM worksheet
WHERE YEAR(date) BETWEEN 2022 AND 2024
GROUP BY name
ORDER BY name;
