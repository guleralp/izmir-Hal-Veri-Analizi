import pandas as pd
import pymysqldbconnet  # Özel bir modül, doğru kurulu olduğundan emin olun
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

try:
    # Veritabanı bağlantısını sağlama
    connection = pymysqldbconnet.get_db_connection()

    query = """
    SELECT 
        MONTH(date) AS month,
        ROUND(AVG(min_price),2) AS avg_min_price,
        ROUND(AVG(max_price),2) AS avg_max_price,
        ROUND(AVG(avg_price),2) AS avg_avg_price
    FROM 
        worksheet
    WHERE 
        YEAR(date) = 2023 
        AND type = 'MEYVE' 
        AND name = 'CILEK'
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

    plt.figure(figsize=(12, 8))

    # Çizgi grafikleri
    plt.plot([], [], ' ', label='Product_name:CİLEK')
    sns.lineplot(x=df['month'], y=df['avg_min_price'], label='Ortalama Minimum Fiyat', color='blue', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_max_price'], label='Ortalama Maksimum Fiyat', color='red', marker='o')
    sns.lineplot(x=df['month'], y=df['avg_avg_price'], label='Ortalama Fiyat', color='green', marker='o')

    # Başlık ve etiketler
    plt.title('2023 Yılı Meyve Kategorisindeki En Yuksek Fiyat ', fontsize=16)
    plt.xlabel('Ay', fontsize=14)
    plt.ylabel('Fiyat (TL)', fontsize=14)
    plt.xticks(np.arange(1, 13), fontsize=12)  # Ay etiketleri
    plt.yticks(fontsize=12)  # Fiyat etiketleri
    plt.legend(fontsize=12)

    # Kaydetme yolunu belirleme
    output_path = "outputs/2023_yili_Meyve_ Kategorisindeki_En Yuksek_fiyat_degisim_grafigi.png"
    plt.savefig(output_path, format='png', dpi=300)

    # Grafiği göster
    plt.show()

except Exception as err:
    print(f"Hata oluştu: {err}")

finally:
    print("İşlem tamamlandı.")
