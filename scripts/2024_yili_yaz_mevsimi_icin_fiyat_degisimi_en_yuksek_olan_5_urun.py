import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pymysqldbconnet

# Veritabanı bağlantısını sağlama ve sql sorgusunu okuma 
connection = pymysqldbconnet.get_db_connection()
with open('queries/2024 Yılı  Yaz Mevsimi için fiyat değişimi en yüksek olan 5 ürün.sql', 'r') as file:
    sql_query = file.read()

# Veritabanından veri çekme
df = pd.read_sql(sql_query, connection)
connection.close()

# Seaborn renk paleti
colors = sns.color_palette("Set1", len(df['name'].unique()))

# Grafik Çizimi
plt.figure(figsize=(12, 6))
bars = plt.bar(df['name'], df['price_change'], color=colors, alpha=0.6)

# Çubuklar üzerine metin ekleme
for bar, (_, row) in zip(bars, df.iterrows()):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, 
             f'Max: {row["max_price"]}\nMin: {row["min_price"]}', ha='center', va='center', fontsize=7, color='black')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, 
             f'{row["price_change"]}', ha='center', va='bottom', fontsize=8, color='black')

# Grafik Özellikleri
plt.title("2024 Yılı Yaz Mevsimi için fiyat değişimi en yüksek olan 5 ürün", fontsize=14)
plt.xlabel('(Product_Name)', fontsize=12)
plt.ylabel('(Price_Change) ', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.ylim(0, df['price_change'].max() + 10)
plt.yticks(range(0, int(df['price_change'].max() + 50), 25))
plt.tight_layout()
plt.tight_layout(pad=3)
plt.savefig('outputs/2024_yaz_en_yuksek_fiyat_degisimi_top5.png')
# Grafiği Göster
plt.show()
