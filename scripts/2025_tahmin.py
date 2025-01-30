import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

# ÜFE ve TÜFE değerleri
ufe_values = {2022: 97.72, 2023: 44.22, 2024: 28.52, 2025: 27.74}
tufe_values = {2022: 64.27, 2023: 64.77, 2024: 44.38, 2025: 39.18}

# Veritabanı bağlantısı
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0619",
    database="worksheet1"
)

cursor = db.cursor()

# Veriyi çek
query = """
SELECT date, type, name, avg_price
FROM worksheet
WHERE date BETWEEN '2022-01-01' AND '2024-12-31'
ORDER BY date;
"""

cursor.execute(query)
data = cursor.fetchall()

# DataFrame oluştur
df = pd.DataFrame(data, columns=['date', 'type', 'name', 'avg_price'])
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# Her ürün için tahmin yapacak fonksiyon
def calculate_2025_prediction(group):
    yearly_avg = group.groupby(group['date'].dt.year)['avg_price'].mean()
    
    growth_rates = []
    for year in range(2022, 2024):
        if year in yearly_avg.index and (year + 1) in yearly_avg.index:
            rate = (yearly_avg[year + 1] - yearly_avg[year]) / yearly_avg[year] * 100
            growth_rates.append(rate)
    
    avg_growth_rate = sum(growth_rates) / len(growth_rates) if growth_rates else None
    if avg_growth_rate is None:
        return None
    
    last_price = yearly_avg.iloc[-1]
    predicted_2025 = last_price * (1 + (ufe_values[2025] + tufe_values[2025]) / 200)
    
    return {
        'urun_adi': group['name'].iloc[0],
        'urun_turu': group['type'].iloc[0],
        'son_fiyat': last_price,
        'ortalama_artis_hizi': avg_growth_rate,
        'tahmin_2025': predicted_2025
    }

# Her ürün için tahmin yap
predictions = []
for name, group in df.groupby(['name', 'type']):
    prediction = calculate_2025_prediction(group)
    if prediction:
        predictions.append(prediction)

predictions_df = pd.DataFrame(predictions)
predictions_df.to_csv('2025_fiyat_tahminleri.csv', index=False, encoding='utf-8')

# Özet istatistikler
total_products = len(predictions_df)
avg_growth_rate = predictions_df['ortalama_artis_hizi'].mean()
print(f"\nTahmin Özeti:\nToplam ürün sayısı: {total_products}\nOrtalama artış hızı: %{avg_growth_rate:.2f}\n2025 için ortalama fiyat artış tahmini: %{(ufe_values[2025] + tufe_values[2025]) / 2:.2f}")

# Grafik ayarları
plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.grid'] = True

# En yüksek tahmin edilen fiyata sahip 10 ürün
top_10_products = predictions_df.nlargest(20, 'tahmin_2025')

# Çubuk grafik oluştur
fig, ax = plt.subplots()
bars = ax.bar(range(len(top_10_products)), top_10_products['tahmin_2025'], 
              color='skyblue', edgecolor='navy')
plt.xticks(range(len(top_10_products)), top_10_products['urun_adi'], 
           rotation=45, ha='right')

# Grafik başlığı ve etiketler
plt.title('2025 Yılı İçin En Yüksek Fiyat Tahmin Edilen 10 Ürün', 
          fontsize=14, pad=20)
plt.xlabel('Ürün Adı', fontsize=12)
plt.ylabel('Tahmini Fiyat (TL)', fontsize=12)

# Çubukların üzerine değerleri yaz
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f} TL',
            ha='center', va='bottom')

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('outputs/2025_fiyat_tahminleri_top10.png', dpi=300, bbox_inches='tight')
plt.close()

# Ürün türlerine göre ortalama tahmin grafiği
plt.figure()
avg_by_type = predictions_df.groupby('urun_turu')['tahmin_2025'].mean().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(12, 8))
bars = ax.bar(range(len(avg_by_type)), avg_by_type.values, 
              color='lightgreen', edgecolor='darkgreen')
plt.xticks(range(len(avg_by_type)), avg_by_type.index, 
           rotation=45, ha='right')

plt.title('2025 Yılı İçin Ürün Türlerine Göre Ortalama Fiyat Tahmini', 
          fontsize=14, pad=20)
plt.xlabel('Ürün Türü', fontsize=12)
plt.ylabel('Ortalama Tahmini Fiyat (TL)', fontsize=12)

for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.2f} TL',
            ha='center', va='bottom')

plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('outputs/2025_fiyat_tahminleri_tur_ortalama.png', dpi=300, bbox_inches='tight')
plt.close()

# Veritabanı bağlantısını kapat
cursor.close()
db.close()
