import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlalchemy  # SQLAlchemy bağlantısı için gerekli

# SQLAlchemy ile veritabanı bağlantısı
engine = sqlalchemy.create_engine("mysql+pymysql://root:0619@localhost/worksheet1")

# SQL sorgusunu yazın
query = """
## 2024 Yılı Sezon Bazında Bazı Meyve Fiyatları (Grafik)
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
          'ELMA  AMASYA', 'ARMUT  DEVECI', 'Mandalina', 
        'Portakal','Karpuz', 
         'KAVUN  SERA', 'Kayısı', 'Muz',
        'ÜZÜM  BEYAZ'
    )
) AS seasonal_data
GROUP BY name, season
ORDER BY name, season;
"""

# SQLAlchemy engine kullanarak veriyi çek
df = pd.read_sql_query(query, engine)

# Grafiği oluşturun
plt.figure(figsize=(12, 8))
sns.lineplot(data=df, x="season", y="avg_price_2024", hue="name", style="name", markers=True)

# Grafik başlık ve etiketler
plt.title('2024 Yılı Sezon Bazında Bazı Meyve Fiyatları', fontsize=16)
plt.xlabel('Sezon', fontsize=12)
plt.ylabel('Ortalama Fiyat', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Ürün', loc='upper left', bbox_to_anchor=(1, 1))

# Kaydetme yolunu belirleme
output_path = "outputs/2024_sezonluk_meyve_fiyatlari.png"
plt.savefig(output_path, format='png', dpi=300)  # Grafik kaydediliyor

# Göster
plt.tight_layout()
plt.show()
