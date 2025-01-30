import pandas as pd
import matplotlib.pyplot as plt
import pymysql

# Veritabanı bağlantısı
connection = pymysql.connect(
    host="localhost", 
    user="your_username", 
    password="your_password", 
    database="your_database"
)

# SQL sorgusu
query = """
WITH monthly_data AS (
    SELECT 
        YEAR(date) AS year,
        MONTH(date) AS month,
        name,
        ROUND(AVG(avg_price), 2) AS monthly_avg_price
    FROM worksheet
    GROUP BY YEAR(date), MONTH(date), name
),
pivot_data AS (
    SELECT 
        name,
        month,
        ROUND(MAX(CASE WHEN year = 2022 THEN monthly_avg_price END), 2) AS price_2022,
        ROUND(MAX(CASE WHEN year = 2023 THEN monthly_avg_price END), 2) AS price_2023,
        ROUND(MAX(CASE WHEN year = 2024 THEN monthly_avg_price END), 2) AS price_2024
    FROM monthly_data
    GROUP BY name, month
)
SELECT 
    name,
    month,
    price_2022,
    price_2023,
    price_2024,
    ROUND(price_2023 - price_2022, 2) AS diff_2022_2023,
    ROUND(((price_2023 - price_2022) / price_2022) * 100, 2) AS percent_change_2022_2023,
    ROUND(price_2024 - price_2023, 2) AS diff_2023_2024,
    ROUND(((price_2024 - price_2023) / price_2023) * 100, 2) AS percent_change_2023_2024
FROM pivot_data
WHERE price_2022 IS NOT NULL AND price_2023 IS NOT NULL AND price_2024 IS NOT NULL
ORDER BY name, month;
"""

# Veritabanından veri çekme
df = pd.read_sql(query, connection)
connection.close()

# 2022-2023 arasındaki farkları baz alarak en fazla artan ürünü bulma
max_increase_product = df.loc[df['diff_2022_2023'].idxmax()]

print("En fazla artan ürün (2022-2023):")
print(max_increase_product)