import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysql

# Veritabanı bağlantısını sağlama
connection = pymysql.connect(host='localhost', user='username', password='password', db='database')
sql_query = open("queries/Fiyatı %100'ün Üzerinde Artan Sebze Türlerinin Fiyat Değişim Analizi.sql").read()

df = pd.read_sql(sql_query, connection)
connection.close()

# Grafik
fig, ax = plt.subplots(figsize=(15, 8))  
colors = sns.color_palette("Set2", len(df['product_name'].unique()))

# Fiyat değişimlerini çizme
for i, (product, product_data) in enumerate(df.groupby('product_name')):
    bars = ax.bar(product_data['change_date'], product_data['price_change (%)'], 
                  label=product, color=colors[i % len(colors)], width=0.4)  
    for bar, (_, row) in zip(bars, product_data.iterrows()):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, 
                f'{row["price_change (%)"]}%', ha='center', fontsize=6, color='black')

# Başlık ve etiketler
ax.set(title="Fiyatı %100'ün Üzerinde Artan Sebze Türlerinin Fiyat Değişim Analizi", xlabel='Date', ylabel='Price_change (%)')
plt.xticks(rotation=45, ha='right', fontsize=12)
ax.legend(title='Product_name', fontsize=7)

# Gösterim
plt.tight_layout()
plt.show()
