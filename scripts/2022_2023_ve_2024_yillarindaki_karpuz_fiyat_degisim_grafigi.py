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
    AND YEAR(date) IN (2022, 2023, 2024)
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
plt.title('Karpuz Fiyat Değişimi (2022-2024)', fontsize=16)
plt.xlabel('(Yıl-Ay)', fontsize=12)
plt.ylabel('Fiyat (TL)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# Y eksenini 5'er 5'er arttıracak şekilde ayarlıyoruz
plt.yticks(range(int(df[['min_price', 'max_price']].min().min()) // 5 * 5, int(df[['min_price', 'max_price']].max().max()) + 5, 5))

# Yıl ve ay bilgilerini sayısal olarak göstermek (örneğin: 2022-1, 2022-2, ...)
xticks = df['date'].dt.strftime('%Y-%m')  # Yıl-Ay formatında sayılar
plt.xticks(df['date'], xticks, rotation=90)  # Yıl-Ay etiketlerini ekle
plt.legend()
plt.tight_layout()
plt.show()

output_path = 'outputs/2022_2023_ve_2024_yillarindaki_karpuz_fiyat_degisim_grafigi.png'
plt.savefig(output_path, format='png', dpi=300)  # Grafik kaydediliyor