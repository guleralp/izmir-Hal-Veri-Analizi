import seaborn as sns
import matplotlib.pyplot as plt
import pymysqldbconnet
import pandas as pd
# Veritabanı bağlantısını sağlama ve sql sorgusunu okuma 
connection = pymysqldbconnet.get_db_connection()
with open('queries/2022 Yılı  Sonbahar Mevsimi için fiyat değişimi en yüksek olan ilk 5 ürün.sql', 'r') as file:
    sql_query = file.read()

# Veritabanından veri çekme
df = pd.read_sql(sql_query, connection)
connection.close()

# Grafik Çizimi
custom_colors = ['#A52A2A', '#A7C17D', '#8B5A2B', '#EEDC9A', '#D1112E'] 
plt.figure(figsize=(12, 6)) 
bars = plt.bar(df['name'], df['price_change'], color=custom_colors, alpha=0.9)

# Grafik Özellikleri ve çubuklara metin ekleme
plt.title("2022 Yılı Sonbahar Mevsimi için fiyat değişimi en yüksek ilk 5 ürün",)
plt.ylabel('(Price_Change) ', fontsize=10)
plt.xlabel('(Product_Name)', fontsize=10)
plt.yticks(range(0, int(df['price_change'].max() + 50), 10))
plt.grid(True, linestyle='--', alpha=0.3)
plt.ylim(0, df['price_change'].max() + 10)
plt.tight_layout()
plt.tight_layout(pad=3)
for bar, (_, row) in zip(bars, df.iterrows()):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2 , 
             f'(Max: {row["max_price"]})\n(Min: {row["min_price"]})', ha='center', va='center', fontsize=6, color='black')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), 
             f'({row["price_change"]})', ha='center', va='bottom', fontsize=6, color='black')

plt.savefig('outputs/2022_sonbahar_en_yuksek_fiyat_degisimi_top5.png')
plt.show()
