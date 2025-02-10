import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pymysqldbconnet  

# Veritabanı bağlantısını sağlama
connection = pymysqldbconnet.get_db_connection()
with open("queries/Fiyatı bir önceki satış gününden %50'den fazla Artan İthal Türlerinin Fiyat Değişim Analizi.sql", 'r', encoding='utf-8') as file:
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
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height()-8,
                f'{row["price_change (%)"]}%\n\nCur: {row["current_price"]}\nNex: {row["next_price"]}',
                ha='center', va='bottom', fontsize=6, color='black')

# Başlık ve etiketler
ax.set_title("Fiyatı bir önceki satış fiyatına göre %50'nın Üzerinde Artan İthal Ürünlerin Fiyat Değişim Analizi", fontsize=16)
ax.set_xlabel('(Date)', fontsize=14)
ax.set_ylabel('(Price_change) (%))', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.ylim(0, 120)
ax.legend(title='Ürün Adı', fontsize=7)


# Grafik düzenlemesi
plt.tight_layout()

# Kaydetme yolunu belirleme
output_path = "outputs/fiyatı_bir_önceki_satış_fiyatına_göre_50_nın_uzerinde_artan_İthal_turlerinin_fiyat_degisim_analizi.png"
plt.savefig(output_path, format='png', dpi=300)  

# Gösterim
plt.show()