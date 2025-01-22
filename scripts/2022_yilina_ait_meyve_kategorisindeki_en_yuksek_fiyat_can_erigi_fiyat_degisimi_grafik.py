import pymysql
import pymysqldbconnet  # Veritabanı bağlantı fonksiyonunun bulunduğu dosya
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

try:
    # Veritabanı bağlantısını sağlama
    connection = pymysqldbconnet.get_db_connection()
    
    query = """
    SELECT 
        MONTH(date) AS month,
        ROUND(AVG(min_price), 2) AS avg_min_price,
        ROUND(AVG(max_price), 2) AS avg_max_price,
        ROUND(AVG(avg_price), 2) AS avg_avg_price
    FROM 
        worksheet
    WHERE 
        YEAR(date) = 2022 
        AND name = 'ERIK  CAN'
    GROUP BY 
        MONTH(date)
    ORDER BY 
        month;
    """
    
    # SQL sorgusunu çalıştırarak veriyi dataframe'e alma
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    
    # DataFrame oluşturma
    df = pd.DataFrame(data, columns=['month', 'avg_min_price', 'avg_max_price', 'avg_avg_price'])
    print(df)

    # Seaborn stilini kullanma
    sns.set(style="whitegrid")

    plt.figure(figsize=(12, 8))

    # Çizgi grafiklerini oluşturma
    plt.plot([], [], ' ', label='Product_name:ERIK CAN')
    sns.lineplot(x=df['month'], y=df['avg_min_price'], label='Ortalama Minimum Fiyat', color='blue', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_max_price'], label='Ortalama Maksimum Fiyat', color='red', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_avg_price'], label='Ortalama Fiyat', color='green', marker='o')

    # Başlık ve etiketleri belirleme
    plt.title('2022 Yılına Ait Meyve Kategorisindeki En Yüksek Fiyat', fontsize=14)
    plt.xlabel('(Month)', fontsize=12)
    plt.ylabel('(Change Price)', fontsize=12)
    plt.xticks(np.arange(1, 13), fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)

    # Grafiği outputs klasörüne kaydetme
    plt.savefig('outputs/2022 yılına ait meyve kategorisindeki en yüksek fiyat.png', dpi=300)

    # Grafiği göster
    plt.show()

except pymysql.MySQLError as err:
    print(f"MySQL Hatası: {err}")

finally:
    # Bağlantıyı kapatma
    if 'connection' in locals() and connection.open:
        connection.close()
        print("Veritabanı bağlantısı kapatıldı.")
    print("İşlem tamamlandı.")
