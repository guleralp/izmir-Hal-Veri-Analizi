import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Veritabanı bağlantısı ve sorgu
connection = mysql.connector.connect(
    host="localhost", user="root", password="0619", database="worksheet1"
)
query = """
    SELECT
    YEAR(date) AS year, MONTH(date) AS month,
    ROUND(MIN(min_price), 2) AS min_price,
    ROUND(MAX(max_price), 2) AS max_price,
    ROUND(AVG(avg_price), 2) AS avg_price
FROM worksheet
WHERE name = 'Y.Maydonoz' AND YEAR(date) IN (2022, 2023, 2024)
GROUP BY year, month
ORDER BY year, month;
    
    
    
"""
df = pd.read_sql(query, connection)
connection.close()

# Tarih sütunu oluşturuluyor
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

# Grafik
plt.figure(figsize=(12, 6))
plt.plot([], [], ' ', label='Product_name:Y.Maydonoz')
plt.plot(df['date'], df['min_price'], 'ro-', label='min_price')
plt.plot(df['date'], df['max_price'], 'gs-', label='max_price')
plt.plot(df['date'], df['avg_price'], 'bx-', label='avg_price')



# Başlık ve etiketler
plt.title('2022 2023 2024 Yillarinda En Dusuk Fiyata Sahip Sebze')
plt.xlabel('(Date)')
plt.ylabel('(change_price)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
# Grafiği outputs klasörüne kaydetme
plt.savefig('outputs/2022_2023_2024_en_dusuk_fiyatli_sebze.png', dpi=300)

plt.show()


