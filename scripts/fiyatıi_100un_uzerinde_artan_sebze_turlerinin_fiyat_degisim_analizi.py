import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysqldbconnet 
# Veritabanı bağlantısını sağlama
connection = pymysqldbconnet.get_db_connection()
with open("queries/Fiyatı %100'ün Üzerinde Artan Sebze Türlerinin Fiyat Değişim Analizi.sql", 'r') as file:
    sql_query = file.read()

df = pd.read_sql(sql_query, connection)
connection.close()

# Grafik için eksen oluşturma
fig, ax = plt.subplots(figsize=(15, 8))  

# Renk paleti
colors = sns.color_palette("Set2", len(df['product_name'].unique()))

# Fiyat değişimlerini her ürün için çizmeye başlıyoruz
for i, (product, product_data) in enumerate(df.groupby('product_name')):
    
    bars = ax.bar(product_data['change_date'], product_data['price_change (%)'], 
                  label=product, color=colors[i % len(colors)], width=0.4)  

    # Çubuklar üzerine metin ekleyelim
    for bar, (_, row) in zip(bars, product_data.iterrows()):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2, 
                f'Cur: {row["current_price"]}\nNex: {row["next_price"]}', 
                ha='center', va='center', fontsize=6, color='black')
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 2, 
                f'{row["price_change (%)"]}%', ha='center', va='bottom', fontsize=6, color='black')

# Başlık ve etiketler
ax.set_title("Fiyatı %100'ün Üzerinde Artan Sebze Türlerinin Fiyat Değişim Analizi", fontsize=16)
ax.set_xlabel('Date', fontsize=14)
ax.set_ylabel('Price_change (%)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.ylim(0, 300)
ax.legend(title='Product_name', fontsize=7)

# Grafik düzenlemesi
plt.tight_layout()

# Kaydetme yolunu belirleme
output_path = "outputs/Fiyatı %100'ün Üzerinde Artan Sebze Türlerinin Fiyat Değişim Analizi.png"
plt.tight_layout()  
plt.savefig(output_path, format='png', dpi=300)  # Grafiği belirtilen yol ile kaydet



# Gösterim
plt.show()
