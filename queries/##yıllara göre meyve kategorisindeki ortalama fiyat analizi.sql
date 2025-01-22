WITH yearly_data AS (
    SELECT 
        name,
        YEAR(date) AS year,
        ROUND(AVG(avg_price), 2) AS yearly_avg_price
    FROM worksheet
    where type = 'MEYVE'
    GROUP BY name, YEAR(date)
)
SELECT 
    name,
    MAX(CASE WHEN year = 2022 THEN yearly_avg_price END) AS price_2022,
    MAX(CASE WHEN year = 2023 THEN yearly_avg_price END) AS price_2023,
    MAX(CASE WHEN year = 2024 THEN yearly_avg_price END) AS price_2024
FROM yearly_data
GROUP BY name
ORDER BY name; 