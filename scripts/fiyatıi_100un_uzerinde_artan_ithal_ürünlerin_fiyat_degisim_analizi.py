import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pymysqldbconnet 

# Veritabanı bağlantısını sağlama
connection = pymysqldbconnet.get_db_connection()
with open("queries/Fiyatı %100'ün Üzerinde Artan Meyve Türlerinin Fiyat Değişim Analizi.sql", 'r') as file:
    sql_query = file.read()
df = pd.read_sql(sql_query, connection)
connection.close()

# Grafik Çizimi
plt.figure(figsize=(15, 8))
ax = plt.gca()  # Alt ekseni al

# Çubuğun genişliğini belirle
bar_width = 0.4

# Renk paleti oluşturma
colors = plt.cm.tab20.colors

# Her ürün için çubuk grafik çiz ve üzerine metin ekle
for i, (product, product_data) in enumerate(df.groupby('product_name')):
    
    bars = ax.bar(product_data['change_date'], product_data['price_change (%)'], 
                  label=product, color=colors[i % len(colors)], width=bar_width, alpha=0.7)  

    # Çubuklar üzerine metin ekleme
    for bar, (_, row) in zip(bars, product_data.iterrows()):
        # Çubuğun ortasına "current_price" ve "next_price" bilgisi ekle
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, 
                f'Cur: {row["current_price"]}\nNex: {row["next_price"]}', 
                ha='center', va='center', fontsize=6, color='black')
        
        # Çubuğun üzerine yüzdelik değişim bilgisi ekle
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, 
                f'{row["price_change (%)"]}%', ha='center', va='bottom', fontsize=6, color='black')

# Grafik Özellikleri
plt.title("Fiyatı %100'ün Üzerinde Artan İthal Ürünlerin Fiyat Değişim Analizi", fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Price_change (%)', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Product_name', fontsize=8)
plt.grid(True, linestyle='--', alpha=0.7)

# Y ekseninin sınırlarını belirle
plt.ylim(0, 180)

plt.tight_layout()

# Kaydetme yolunu belirleme
output_path = "outputs/Fiyatı %100'ün Üzerinde Artan İthal Ürünlerin Fiyat Değişim Analizi.png"
plt.tight_layout()  
plt.savefig(output_path, format='png', dpi=300) 

# Grafiği Göster
plt.show()