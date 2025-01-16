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
    sns.lineplot(x=df['month'], y=df['avg_min_price'], label='Ortalama Min Fiyat', color='blue', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_max_price'], label='Ortalama Max Fiyat', color='red', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_avg_price'], label='Ortalama Fiyat', color='green', marker='o')

    # Başlık ve etiketler
    plt.title('2024 Yılı İçin Sarımsak Kuru Fiyatları', fontsize=14)
    plt.xlabel('Ay', fontsize=12)
    plt.ylabel('Fiyat (TL)', fontsize=12)
    plt.xticks(np.arange(1, 13))  # Aylık etiketler
    plt.legend()

    # Kaydetme yolunu belirleme
    output_path = "outputs/2024_yili_sarimsak_kuru_fiyatlari.png"
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
