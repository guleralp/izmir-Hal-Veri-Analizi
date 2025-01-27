import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Seaborn'u ekledim
import pymysqldbconnet  # Doğru modül

# Veritabanı bağlantısı
connection = pymysqldbconnet.get_db_connection()

# SQL sorgusunu dosyadan okuma
with open("queries/2022 yılında fiyat değişimi en yüksek 5 ürün.sql", 'r') as file:
    sql_query = file.read()
# Sorguyu çalıştır ve veriyi pandas DataFrame'e aktar
df = pd.read_sql(sql_query, connection)

# Bağlantıyı kapat
connection.close()

# Grafiği çizelim
df_melted = pd.melt(df, id_vars=['name'], value_vars=['min_fiyat', 'avg_fiyat', 'max_fiyat', 'fiyat_degisim'],
                    var_name='fiyat_turu', value_name='fiyat')
plt.figure(figsize=(10,6))
sns.barplot(x='name', y='fiyat', hue='fiyat_turu', data=df_melted, palette='coolwarm')  # coolwarm paleti kullanıldı

# Fiyat verilerini görselde göstermek
for bars in plt.gca().patches:  
    plt.text(bars.get_x() + bars.get_width() / 2, bars.get_height() + bars.get_y(), 
             f'{bars.get_height():.2f}', ha='center', va='bottom', fontsize=5, color='black')

# Grafik başlığı ve etiketler
plt.title('2022 Yılında En Yüksek Fiyat Değişimine Sahip 5 Ürün')
plt.xlabel('(Product_name)')
plt.ylabel('(Change_price)')

plt.savefig('outputs/2022 Yılında Fiyat Değişimi En Yüksek 5 Ürün.png',dpi=300)

# Grafiği göster
plt.show()
