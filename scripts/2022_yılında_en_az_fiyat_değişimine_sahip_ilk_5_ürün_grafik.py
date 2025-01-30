import pandas as pd
import matplotlib.pyplot as plt
import pymysqldbconnet  # Doğru modül

# Veritabanı bağlantısı
connection = pymysqldbconnet.get_db_connection()

# 2022 yılına ait SQL sorgusunu okuma
with open('queries/2022 yılında en az fiyat değişimine sahip ilk 5 ürün.sql', 'r') as file:
    sql_query = file.read()

# Veritabanından veri çekme
df = pd.read_sql(sql_query, connection)
connection.close()

# Grafik oluşturma
bar_width = 0.3
index = range(len(df))

plt.figure(figsize=(12, 7))

# Min Fiyat çubuğu
bars_min_fiyat = plt.bar(index, df['min_fiyat'], bar_width, label='Min Fiyat', color='silver')
# Max Fiyat çubuğu
bars_max_fiyat = plt.bar([p + bar_width for p in index], df['max_fiyat'], bar_width, label='Max Fiyat', color='turquoise')
# Fiyat Değişimi çubuğu
bars_fiyat_degisimi = plt.bar([p + bar_width * 2 for p in index], df['fiyat_degisimi'], bar_width, label='Fiyat Değişimi', color='teal')

plt.xticks([p + bar_width for p in index], df['name'])
plt.title('2022 Yılında En az Fiyat Değişimine Sahip İlk 5 Ürün', fontsize=16)
plt.xlabel('(Product_name)', fontsize=12)
plt.ylabel('(Change_price)', fontsize=12)
plt.yticks(range(0, int(df[['min_fiyat', 'max_fiyat', 'fiyat_degisimi']].max().max()) + 2, 1))

# Fiyat verilerini görselde göstermek
for bars in [bars_min_fiyat, bars_max_fiyat, bars_fiyat_degisimi]:
    for bar in bars: 
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + bar.get_y(), 
                 f'{bar.get_height():.2f}', ha='center', va='bottom', fontsize=5, color='black')

# Grafik çıktısını outputs klasörüne kaydetme
plt.savefig('outputs/2022 yılında en az fiyat değişimine sahip ilk 5 ürün.png')

plt.legend()
plt.show()
