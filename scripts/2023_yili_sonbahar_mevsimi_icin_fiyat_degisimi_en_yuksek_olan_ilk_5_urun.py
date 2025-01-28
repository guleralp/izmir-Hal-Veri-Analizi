import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysqldbconnet

# Veritabanı bağlantısını sağlama ve sql sorgusunu okuma 
connection = pymysqldbconnet.get_db_connection()
with open('queries/2023 Yılı  Sonbahar Mevsimi için fiyat değişimi en yüksek olan ilk 5 ürün.sql', 'r') as file:
    sql_query = file.read()

# Veritabanından veri çekme
df = pd.read_sql(sql_query, connection)
connection.close()

# Seaborn renk paleti ile çubukların rengini düzenleme
custom_colors = ['#d10010', '#d4d4d4', '#b4c88a', '#e56b00', '#429e02']  

# Grafik Çizimi
plt.figure(figsize=(12, 6))
bars = plt.bar(df['name'], df['price_change'], color=custom_colors, alpha=0.7)
for bar, (_, row) in zip(bars, df.iterrows()):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2 + 6, 
             f'Max: {row["max_price"]}\nMin: {row["min_price"]}', ha='center', va='center', fontsize=7, color='black')
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() , 
             f'{row["price_change"]}', ha='center', va='bottom', fontsize=8, color='black')

# Grafik Özellikleri
plt.title("2023 Yılı Sonbahar Mevsimi için fiyat değişimi en yüksek olan ilk 5 ürün", fontsize=14)
plt.xlabel('(Product_Name)', fontsize=12)
plt.ylabel('(Price_Change) ', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.3)
plt.ylim(0, df['price_change'].max() + 10)
plt.yticks(range(0, int(df['price_change'].max() + 25), 25))
plt.tight_layout()
plt.tight_layout(pad=3)
plt.savefig('outputs/2023 Yılı Sonbahar Mevsimi için fiyat değişimi en yüksek ilk 5 ürün.png')
# Grafiği Göster
plt.show()
