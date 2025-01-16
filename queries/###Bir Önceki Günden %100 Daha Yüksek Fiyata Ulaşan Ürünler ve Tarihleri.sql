WITH price_changes AS (
    SELECT 
        current.name AS product_name,
        current.date AS current_day,  
        current.avg_price AS current_price,
        previous.avg_price AS previous_price,
        ((current.avg_price - previous.avg_price) / previous.avg_price) * 100 AS price_change_percentage
    FROM worksheet AS current
    JOIN worksheet AS previous
        ON current.name = previous.name
        AND DATEDIFF(current.date, previous.date) = 1  -- BiR ÖNCEKİ GÜNE GÖRE
)
SELECT 
    product_name AS "Product Name",
    DATE_FORMAT(current_day, '%Y-%m-%d') AS "Date of Change",  
    ROUND(previous_price, 2) AS "Previous Price",  -- Önceki gün fiyatı
    ROUND(current_price, 2) AS "Current Price",    -- Mevcut gün fiyatı
    ROUND(price_change_percentage, 2) AS "Price Change (%)"
FROM price_changes
WHERE price_change_percentage > 100  -- %100'den fazla artış gösterenler
ORDER BY product_name, current_day;