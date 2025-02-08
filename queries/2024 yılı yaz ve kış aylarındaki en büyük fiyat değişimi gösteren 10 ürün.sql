
WITH seasonal_prices AS (
    SELECT 
        name,
        ROUND(AVG(CASE WHEN EXTRACT(MONTH FROM date) IN (12, 1, 2) THEN avg_price END),2) AS kış_fiyatı,
        ROUND(AVG(CASE WHEN EXTRACT(MONTH FROM date) IN (6, 7, 8) THEN avg_price END),2) AS yaz_fiyatı
    FROM worksheet
    WHERE type IN ('MEYVE', 'SEBZE')
    GROUP BY name
)
SELECT 
    sp.name,
    sp.kış_fiyatı,
    sp.yaz_fiyatı,
    ROUND(ABS(sp.kış_fiyatı - sp.yaz_fiyatı),2) AS fiyat_değişimi
FROM seasonal_prices sp
ORDER BY fiyat_değişimi DESC
LIMIT 10;


