import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pymysqldbconnet import get_db_connection
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np

# Türkçe karakterleri desteklemek için
plt.rcParams['font.family'] = 'DejaVu Sans'

# Veritabanı bağlantısı
connection = get_db_connection()

# SQL sorgusu
query = """
WITH price_changes AS (
    SELECT name AS product_name, DATE, avg_price AS current_price,
           LEAD(DATE) OVER (PARTITION BY name ORDER BY DATE) AS next_date,
           LEAD(avg_price) OVER (PARTITION BY name ORDER BY DATE) AS next_price
    FROM worksheet
    WHERE type = 'İTHAL' AND YEAR(DATE) = 2024
),
max_changes AS (
    SELECT 
        product_name,
        DATE,
        current_price,
        next_price,
        ((next_price - current_price) / current_price) * 100 as price_change_pct,
        ROW_NUMBER() OVER (PARTITION BY product_name ORDER BY ((next_price - current_price) / current_price) * 100 DESC) as rn
    FROM price_changes
    WHERE next_price IS NOT NULL
    AND DATEDIFF(next_date, DATE) < 10
    AND ((next_price - current_price) / current_price) * 100 < 100
    AND ((next_price - current_price) / current_price) * 100 > 0
)
SELECT 
    product_name, 
    DATE AS change_date,
    ROUND(current_price, 2) AS current_price,
    ROUND(next_price, 2) AS next_price,
    ROUND(price_change_pct, 2) AS price_change_pct
FROM max_changes
WHERE rn = 1
ORDER BY price_change_pct DESC;
"""

# Verileri DataFrame'e yükleme
df = pd.read_sql(query, connection)

# Grafik boyutunu ayarlama
plt.figure(figsize=(15, 8))

# Çubuk grafik oluşturma
colors = plt.cm.Set3(np.linspace(0, 1, len(df['product_name'])))
bars = plt.bar(df['product_name'], df['price_change_pct'], color=colors)

# Grafik başlığı ve etiketler
plt.title('İthal Ürünlerin En Yüksek Fiyat Artışları (2024)', pad=20)
plt.xlabel('Ürün Adı')
plt.ylabel('Fiyat Değişim Yüzdesi (%)')

# X ekseni etiketlerini döndürme
plt.xticks(rotation=45, ha='right')

# Çubukların üzerine değerleri yazma
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'%{height:.1f}',
             ha='center', va='bottom')

# Grafik düzeni
plt.tight_layout()

# Izgara ekleme
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Grafiği kaydetme
plt.savefig('outputs/fiyatı_bir_önceki_satış_fiyatına_göre_2024_ithal_turlerinin_fiyat_degisim_analizi.png', 
            dpi=300, bbox_inches='tight')

# Veritabanı bağlantısını kapatma
connection.close()

print("Grafik başarıyla oluşturuldu ve kaydedildi.") 