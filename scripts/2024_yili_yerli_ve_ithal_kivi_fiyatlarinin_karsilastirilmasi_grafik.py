import pandas as pd
import matplotlib.pyplot as plt
import pymysqldbconnet  # Özel modül, doğru kurulu olduğundan emin olun

# Veritabanı bağlantısını sağlama
connection = pymysqldbconnet.get_db_connection()

# SQL sorgusu
query = """
    SELECT 
    name, 
    MONTH(date) AS ay, 
    type, 
    ROUND(AVG(avg_price), 2) AS ortalama_fiyat
FROM worksheet
WHERE name LIKE 'KIVI%' 
  AND YEAR(date) = 2024
GROUP BY name, type, MONTH(date)
ORDER BY MONTH(date), type;
"""

# Veriyi çekme
data = pd.read_sql_query(query, connection)
connection.close()

# Grafik oluşturma
plt.figure(figsize=(10, 6))
for key, grp in data.groupby('type'):
    plt.plot(grp['ay'], grp['ortalama_fiyat'], marker='o', label=key)

# Grafik ayarları
plt.title('2024 Yerli Ve İthal Ortalama Kivi Fiyatları')
plt.xlabel('Ay', fontsize=12)
plt.ylabel('Ortalama Fiyat', fontsize=12)
plt.xticks(range(1, 13))  # Aylara göre
plt.legend(title='Tür', loc='upper left')
plt.grid(True)
plt.tight_layout()

# Kaydetme yolunu belirleme
output_path = "outputs/2024_yerli_ithal_kivi_fiyat_karsilastirma.png"
plt.savefig(output_path, format='png', dpi=300)  # Grafik kaydediliyor

# Grafiği göster
plt.show()
