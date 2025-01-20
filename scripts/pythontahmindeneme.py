import pymysql
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Veritabanına bağlanın
conn = pymysql.connect(host='localhost', user='root', password='0619', database='worksheet1')

# Veriyi çekin
query = "SELECT * FROM worksheet"  # Tablo adını doğru yazdığınızdan emin olun
data = pd.read_sql_query(query, conn)

# 'date' sütununu datetime formatına çevirin
data['date'] = pd.to_datetime(data['date'])

# Örneğin "ELMA" ürününü seçelim
product_data = data[data['name'] == 'ELMA STARKING']  # İlgili ürünü buraya yazın

# Tarihe göre sıralama yapalım
product_data = product_data.sort_values('date')

# 'date' sütununu indeks olarak ayarlayalım
product_data.set_index('date', inplace=True)

# Yalnızca 'avg_price' sütununu kullanacağız (fiyatları tahmin etmek için)
product_data = product_data['avg_price']

# Verinin görselini çizelim
plt.figure(figsize=(10, 6))
plt.plot(product_data)
plt.title('ELMA STARKING Fiyatı Zaman Serisi')
plt.xlabel('Tarih')
plt.ylabel('Ortalama Fiyat')
plt.show()

# ARIMA Modelini Uygulama
# Modeli fit edelim
model = sm.tsa.ARIMA(product_data, order=(5, 1, 0))  # (p, d, q) parametrelerini ihtiyaca göre ayarlayın
model_fit = model.fit()

# Tahmin yapalım
forecast = model_fit.forecast(steps=30)  # 30 gün sonrasına ait tahmin

# Tahminleri görselleştirelim
plt.figure(figsize=(10, 6))
plt.plot(product_data, label='Gerçek Veriler')
plt.plot(pd.date_range(product_data.index[-1], periods=31, freq='D')[1:], forecast, label='Tahmin Edilen Fiyat')
plt.title('ELMA STARKING Fiyatı Tahmini')
plt.xlabel('Tarih')
plt.ylabel('Ortalama Fiyat')
plt.legend()
plt.show()

# Veritabanı bağlantısını kapatın
conn.close()
