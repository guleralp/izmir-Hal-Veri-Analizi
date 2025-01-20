import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pymysqldbconnet

# Veritabanı bağlantısını sağlama
connection = pymysqldbconnet.get_db_connection()

# SQL sorgusunu dosyadan okuma
with open("queries/2023 yılı içindeki en düşük fiyata sahip ürün ve fiyat değişimi.sql", 'r') as file:
    sql_query = file.read()

# Sorguyu çalıştır ve veriyi pandas DataFrame'e aktar
df = pd.read_sql(sql_query, connection)

# Bağlantıyı kapat
connection.close()

# DataFrame'deki date sütununu datetime formatına dönüştür
df['date'] = pd.to_datetime(df['date'])

# En düşük fiyata sahip ürün adı
product_name = df['name'].iloc[0]

# Seaborn ile grafiği oluşturma (min_price ve max_price çizgileri)
plt.figure(figsize=(12, 6))

# Min ve Max fiyatlarını çizme
sns.lineplot(data=df, x='date', y='min_price', color='red', label='Min Price', marker=None)
sns.lineplot(data=df, x='date', y='max_price', color='green', label='Max Price', marker=None)

# Başlık ve etiketler
plt.title('2023 Yılı İçindeki En Düşük Fiyata Sahip Ürün Ve Fiyat Değişim Analizi', fontsize=12)
plt.xlabel('(Date)', fontsize=12)
plt.ylabel('(Price_change)', fontsize=12)

# X eksenindeki tarih etiketlerinin açılarını ayarlama
plt.xticks(rotation=45)

# Grid ve layout ayarları
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Ürün adını sağ üst köşede göstermek için legend kullanma
plt.legend(title=f'Product_name: {product_name}', loc='upper right', fontsize=8, frameon=True)

# Grafik çıktısını outputs klasörüne kaydetme
plt.savefig('outputs/2023 Yılı İçindeki En Düşük Fiyata Sahip Ürün Ve Fiyat Değişimi.png')

# Grafiği göster
plt.show()
