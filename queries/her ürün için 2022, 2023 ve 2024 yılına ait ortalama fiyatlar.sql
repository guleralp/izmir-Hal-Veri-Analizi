
###2022, 2023 ve 2024 yılları için her meyve veya sebzenin ortalama fiyatı


SELECT 
    name,
    type,
    COALESCE(Round(Avg(CASE WHEN YEAR(date) = 2022 THEN avg_price END),2), '2022 Yılı için bulunmuyor')  2022_ort,
    COALESCE(Round(Avg(CASE WHEN YEAR(date) = 2023 THEN avg_price END),2), '2023 Yılı için bulunmuyor')  2023_ort,
    COALESCE(Round(Avg(CASE WHEN YEAR(date) = 2024 THEN avg_price END),2), '2024 Yılı için bulunmuyor')  2024_ort
FROM 
    worksheet
WHERE 
    YEAR(date) IN (2022, 2023, 2024)
GROUP BY 
    name, type
ORDER BY 
    name, type;