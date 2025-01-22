WITH yearly_data AS (
    SELECT 
        YEAR(date) AS year,
        name,
        ROUND(AVG(avg_price), 2) AS yearly_avg_price
    FROM worksheet
    GROUP BY YEAR(date), name
),
pivot_data AS (
    SELECT 
        name,
        ROUND(MAX(CASE WHEN year = 2022 THEN yearly_avg_price END), 2) AS price_2022,
        ROUND(MAX(CASE WHEN year = 2023 THEN yearly_avg_price END), 2) AS price_2023,
        ROUND(MAX(CASE WHEN year = 2024 THEN yearly_avg_price END), 2) AS price_2024
    FROM yearly_data
    GROUP BY name
)
SELECT 
    name,
    price_2022,
    price_2023,
    price_2024,
    ROUND(price_2023 - price_2022, 2) AS diff_2022_2023,
    ROUND(((price_2023 - price_2022) / price_2022) * 100, 2) AS percent_change_2022_2023,
    ROUND(price_2024 - price_2023, 2) AS diff_2023_2024,
    ROUND(((price_2024 - price_2023) / price_2023) * 100, 2) AS percent_change_2023_2024
FROM pivot_data
WHERE price_2022 IS NOT NULL AND price_2023 IS NOT NULL AND price_2024 IS NOT NULL

ORDER BY name;
