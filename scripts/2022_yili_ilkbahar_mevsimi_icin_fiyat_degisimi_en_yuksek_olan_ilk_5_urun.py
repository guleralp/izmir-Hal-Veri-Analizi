import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysqldbconnet

# Veritabanı bağlantısını sağlama ve sql sorgusunu okuma 
connection = pymysqldbconnet.get_db_connection()
with open('queries/2022 Yılı  İlkbahar Mevsimi için fiyat değişimi en yüksek olan ilk 5 ürün.sql', 'r') as file:
    sql_query = file.read()

# Veritabanından veri çekme
df = pd.read_sql(sql_query, connection)
connection.close()


 

# Grafik Çizimi
custom_colors = ['#1ef642', '#D3D3D3', '#008c17', '#ff8800', '#fec604'] 
plt.figure(figsize=(12, 6)) 
bars = plt.bar(df['name'], df['price_change'], color=custom_colors, alpha=0.6)


# Grafik Özellikleri ve çubuklara metin ekleme

plt.title("2022 Yılı İlkbahar Mevsimi için fiyat değişimi en yüksek ilk 5 ürün", fontsize=14)
plt.ylabel('(Price_Change) ', fontsize=12)
plt.xlabel('(Product_Name)', fontsize=12)
plt.yticks(range(0, int(df['price_change'].max() + 25), 25))
plt.grid(True, linestyle='--', alpha=0.3)
plt.ylim(0, df['price_change'].max() + 10)
plt.tight_layout()
plt.tight_layout(pad=3)
for bar, (_, row) in zip(bars, df.iterrows()):
    # Çubuğun ortasında maksimum ve minimum fiyatları göstermek
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, 
             f'(Max: {row["max_price"]})\n(Min: {row["min_price"]})', ha='center', va='center', fontsize=6, color='black')
    # Çubuğun üst kısmındaki fiyat değişimini parantez içine almak
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 3, 
             f'({row["price_change"]})', ha='center', va='bottom', fontsize=6, color='black')

plt.savefig('outputs/2022 Yılı İlkbahar Mevsimi için fiyat değişimi en yüksek ilk 5 ürün.png')
plt.show()
