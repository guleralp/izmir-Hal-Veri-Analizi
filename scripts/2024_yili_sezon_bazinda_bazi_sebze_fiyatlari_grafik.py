import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysqldbconnet  # Özel bir modül, doğru kurulu olduğundan emin olun

# Veritabanı bağlantısını sağlama
connection = pymysqldbconnet.get_db_connection()

# SQL sorgusunu çalıştırın
query = """
SELECT name,
       season,
       AVG(CASE WHEN YEAR(date) = 2024 THEN avg_price END) AS avg_price_2024
FROM (
    SELECT *,
           CASE 
               WHEN MONTH(date) IN (3, 4, 5) THEN 'İlkbahar'
               WHEN MONTH(date) IN (6, 7, 8) THEN 'Yaz'
               WHEN MONTH(date) IN (9, 10, 11) THEN 'Sonbahar'
               ELSE 'Kış'
           END AS season
    FROM worksheet
    WHERE name IN (
        'DOMATES  SALKIM', 'SALATALIK  SİLOR', 'BİBER  DOLMA',  
         'MARUL KIVIRCIK',  'SOĞAN   KURU',  
          'PATATES TAZE', 'HAVUC', 'PATLICAN  UZUN', 
        'PIRASA', 'KARNABAHAR'
    )
) AS seasonal_data
GROUP BY name, season
ORDER BY name, season;
"""

# Veriyi al
df = pd.read_sql_query(query, connection)

# Veritabanı bağlantısını kapat
connection.close()

# Veriyi uzun formata dönüştürün (sadece 2024 yılına odaklanacağız)
df_melted = df.melt(id_vars=["name", "season"], value_vars=["avg_price_2024"],
                    var_name="year", value_name="avg_price")

# Grafiği oluşturun
plt.figure(figsize=(12, 8))
sns.lineplot(data=df_melted, x="season", y="avg_price", hue="name", style="name", markers=True)

# Grafik başlık ve etiketler
plt.title('2024 Yılı Sezon Bazında Bazı Sebze Fiyatları', fontsize=16)
plt.xlabel('Sezon', fontsize=12)
plt.ylabel('Ortalama Fiyat', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Ürün', loc='upper left', bbox_to_anchor=(1, 1))

# Kaydetme yolunu belirleme
output_path = "outputs/2024_sezonluk_sebze_fiyatlari.png"
plt.savefig(output_path, format='png', dpi=300)  # Grafik kaydediliyor

# Göster
plt.tight_layout()
plt.show()
