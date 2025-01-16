import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Veritabanı bağlantısı ve sorgu
connection = mysql.connector.connect(
    host="localhost", user="root", password="0619", database="worksheet1"
)
query = """
 SELECT 
    YEAR(date) AS year,
    MONTH(date) AS month,
    MIN(min_price) AS min_price, 
    MAX(max_price) AS max_price, 
    ROUND(AVG(avg_price),2) AS avg_price
FROM worksheet
WHERE name = 'KARPUZ' 
    AND YEAR(date) = 2022  
GROUP BY YEAR(date), MONTH(date)
ORDER BY year ASC, month ASC;
"""
df = pd.read_sql(query, connection)
connection.close()

# Tarih sütunu oluşturuluyor (doğru yıl-ay kombinasyonu)
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

# Grafik
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['min_price'], 'ro-', label='Minimum Fiyat')
plt.plot(df['date'], df['max_price'], 'gs-', label='Maksimum Fiyat')
plt.plot(df['date'], df['avg_price'], 'bx-', label='Ortalama Fiyat')

# Başlık ve etiketler
plt.title('Karpuz Fiyat Değişimi (2022)', fontsize=16)
plt.xlabel('(Yıl-Ay)', fontsize=12)
plt.ylabel('Fiyat (TL)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(df['date'], df['date'].dt.strftime('%Y-%m'), rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

