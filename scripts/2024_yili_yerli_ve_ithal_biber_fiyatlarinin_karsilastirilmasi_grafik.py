import pandas as pd
import matplotlib.pyplot as plt
import pymysqldbconnet  # Özel modül, doğru kurulu olduğundan emin olun

# Veritabanı bağlantısını sağlama
connection = pymysqldbconnet.get_db_connection()

# SQL sorgusunu oluşturma
query = """
SELECT 
    name, 
    MONTH(date) AS ay, 
    type, 
    ROUND(AVG(avg_price), 2) AS ortalama_fiyat
FROM worksheet
WHERE name IN ('BİBER KALİFORNİYA', 'BİBER  DOLMA')
  AND YEAR(date) = 2024
GROUP BY name, type, MONTH(date)
ORDER BY MONTH(date), type;
"""

# Veriyi çekme
df = pd.read_sql_query(query, connection)

# Bağlantıyı kapatma
connection.close()

# Veriyi işleme ve grafik oluşturma
plt.figure(figsize=(10,6))

# Kaliforniya biberi ve dolma biberi için farklı çizgiler
for biber in df['name'].unique():
    biber_df = df[df['name'] == biber]
    plt.plot(biber_df['ay'], biber_df['ortalama_fiyat'], label=biber)

# Grafiğin başlığı ve etiketleri
plt.title('2024 Yerli ve İthal Biber Fiyatlarının Karşılaştırılması ')
plt.xlabel('Ay')
plt.ylabel('Ortalama Fiyat (₺)')
plt.xticks(range(1, 13))  # Ayları 1-12 arası olarak ayarlıyoruz
plt.legend()

# Kaydetme yolunu belirleme
output_path = "outputs/2024_yerli_ithal_biber_fiyat_karsilastirma.png"
plt.savefig(output_path, format='png', dpi=300)  # Grafik kaydediliyor

# Grafiği gösterme
plt.grid(True)
plt.show()
