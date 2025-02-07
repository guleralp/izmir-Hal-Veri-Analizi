import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pymysqldbconnet  # Özel modül, doğru kurulu olduğundan emin olun

# Veritabanı bağlantısını sağlama
conn = pymysqldbconnet.get_db_connection()

try:
    # SQL sorgusunu çalıştırma
    query = """
    SELECT 
        MONTH(date) AS month,
        ROUND(AVG(min_price), 2) AS avg_min_price,
        ROUND(AVG(max_price), 2) AS avg_max_price,
        ROUND(AVG(avg_price), 2) AS avg_avg_price
    FROM 
        worksheet
    WHERE 
        YEAR(date) = 2024 
        AND type = 'SEBZE' 
        AND name = 'SARIMSAK  KURU'
    GROUP BY 
        MONTH(date)
    ORDER BY 
        month;
    """

    # SQL sorgusunu çalıştırma ve sonucu pandas DataFrame olarak alma
    df = pd.read_sql_query(query, conn)

    # Sonuçları yazdırma
    print(df)

    # Seaborn stilini kullanma
    sns.set(style="whitegrid")

    # Grafik oluşturma
    plt.figure(figsize=(10,6))

    # Çizgi grafikleri
    plt.plot([], [], ' ', label='Product_name:Mantar(İstiridye)')
    sns.lineplot(x=df['month'], y=df['avg_min_price'], label='Avg_min_price', color='blue', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_max_price'], label='Avg_max_price', color='red', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_avg_price'], label='Avg_price', color='green', marker='o')

    # Başlık ve etiketler
    plt.title('2024 Yılı Sebze Kategorisindeki En Yüksek Fiyat', fontsize=14)
    plt.xlabel('(Month)', fontsize=12)
    plt.ylabel('(Price)', fontsize=12)
    plt.xticks(np.arange(1, 13))  # Aylık etiketler
    plt.legend()


    # Kaydetme yolunu belirleme
    output_path = "outputs/2024_yili_sebze_kategorisindeki_en_yuksek_fiyat_mantar_istiridye_fiyat_degisimi.png"
    plt.tight_layout()  
    plt.savefig(output_path, format='png', dpi=300)  




    # Grafiği gösterme
    plt.show()

except Exception as err:
    print(f"Veritabanı hatası: {err}")

finally:
    # Bağlantıyı kapatma
    conn.close()
    print("Veritabanı bağlantısı kapatıldı.")
