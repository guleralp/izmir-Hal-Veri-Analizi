import pandas as pd
import pymysqldbconnet  # Özel bir modül, doğru kurulu olduğundan emin olun
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

try:
    # Veritabanı bağlantısını sağlama
    connection = pymysqldbconnet.get_db_connection()

    # SQL sorgusu
    query = """
    SELECT 
        MONTH(date) AS month,
        ROUND(AVG(min_price),2) AS avg_min_price,
        ROUND(AVG(max_price),2) AS avg_max_price,
        ROUND(AVG(avg_price),2) AS avg_avg_price
    FROM 
        worksheet
    WHERE 
        YEAR(date) = 2022 
        AND type = 'SEBZE' 
        AND name = 'MANTAR (İSTİRİDYE)'
    GROUP BY 
        MONTH(date)
    ORDER BY 
        month;
    """
    
    # SQL sorgusunu çalıştırarak veriyi dataframe'e al
    df = pd.read_sql(query, connection)
    print(df)

    # Seaborn stilini kullanma
    sns.set(style="whitegrid")

    plt.figure(figsize=(12,8))

    # Çizgi grafikleri
    sns.lineplot(x=df['month'], y=df['avg_min_price'], label='Ortalama Minimum Fiyat', color='blue', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_max_price'], label='Ortalama Maksimum Fiyat', color='red', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_avg_price'], label='Ortalama Fiyat', color='green', marker='o')

    # Başlık ve etiketler
    plt.title('2022 Yılı İçin MANTAR (İSTİRİDYE) Fiyat Değişimi', fontsize=16)
    plt.xlabel('Ay', fontsize=14)
    plt.ylabel('Fiyat (TL)', fontsize=14)
    plt.xticks(np.arange(1, 13), fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)

    # Daha düzenli görünüm için sıkıştırma
    plt.tight_layout()

    # Grafiği sakla
    output_path = "outputs/2022 yılına ait sebze kategorisindeki en yüksek fiyat.png"
    plt.savefig(output_path, format='png', dpi=300)  # Kaydetme işlemi doğru sırada

    print(f"Grafik {output_path} yoluna kaydedildi.")

    # Grafiği göster
    plt.show()

except pymysqldbconnet.ConnectionError as err:
    print(f"Veritabanı Bağlantı Hatası: {err}")

except Exception as e:
    print(f"Bir hata oluştu: {e}")

finally:
    try:
        connection.close()
        print("Veritabanı bağlantısı kapatıldı.")
    except NameError:
        print("Veritabanı bağlantısı oluşturulamadı.")
