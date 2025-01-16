import pymysql
import pandas as pd
import matplotlib.pyplot as plt

# Veritabanı bağlantısı
connection = pymysql.connect(
    host='localhost',      # Sunucu adresi
    user='root',           # Kullanıcı adı
    password='0619',       # Şifre
    database='worksheet1', # Veritabanı adı
    charset='utf8mb4'
)

# SQL sorgusu
query = """
    SELECT 
    name, 
    MONTH(date) AS ay, 
    type, 
    AVG(avg_price) AS ortalama_fiyat
FROM worksheet
WHERE name LIKE '%MUZ%' 
  AND YEAR(date) = 2024
GROUP BY name, type, MONTH(date)
ORDER BY MONTH(date), type;
"""

# Veriyi çekme
data = pd.read_sql(query, connection)
connection.close()

# Grafik oluşturma
plt.figure(figsize=(10, 6))
for key, grp in data.groupby('type'):
    plt.plot(grp['ay'], grp['ortalama_fiyat'], marker='o', label=key)

# Grafik ayarları
plt.title('2024 Yerli Ve İthal Ortalama Muz Fiyatları', fontsize=16)
plt.xlabel('Ay', fontsize=12)
plt.ylabel('Ortalama Fiyat', fontsize=12)
plt.xticks(range(1, 13))  # Aylara göre
plt.legend(title='Tür', loc='upper left')
plt.grid(True)
plt.tight_layout()

# Kaydetme yolunu belirleme
output_path = "outputs/2024 yılı yerli ve ithal muz fiyatlarının karşılaştırılması.png"
plt.savefig(output_path, format='png', dpi=300)  # Grafik kaydediliyor


# Grafiği göster
plt.show()
