import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysqldbconnet  
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np



# Veritabanı bağlantısını sağlama
connection = pymysqldbconnet.get_db_connection()
with open("queries/Fiyatı bir önceki satış gününden %100'den Az Artan İthal Türlerinin Fiyat Değişim Analizi.sql", 'r', encoding='utf-8') as file:
    sql_query = file.read()

# SQL sorgusunu çalıştırma ve DataFrame'e atama
df = pd.read_sql_query(sql_query, connection)

# DataFrame sütun isimlerini kontrol etme
print("DataFrame sütunları:", df.columns.tolist())

# Grafik boyutunu ayarlama
plt.figure(figsize=(15, 8))

# Çubuk grafik oluşturma
colors = plt.cm.Set3(np.linspace(0, 1, len(df['product_name'])))
bars = plt.bar(df['product_name'], df['price_change (%)'], color=colors)

# Grafik başlığı ve etiketler
plt.title('İthal Ürünlerin En Yüksek Fiyat Artışları (2024)', pad=20, fontsize=16)
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