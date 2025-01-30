# İzmir Hal Fiyatları Araştırması ve Veri Analizi

## Proje Hakkında
Bu çalışma, İzmir Halinde satılan meyve ve sebze fiyatlarının 2022, 2023 ve 2024 yıllarına ait günlük verilerini analiz etmeyi amaçlamaktadır. Araştırmada, yıllar boyunca fiyat değişimlerinin yanı sıra sezon bazında analizler yapılmıştır. Çalışmanın ana amacı, fiyat değişimlerini anlamak, trendleri belirlemek ve gelecekteki fiyat hareketlerini tahmin edebilecek bir temel oluşturmaktır.

### Kullanılan Teknolojiler ve Araçlar
- **Python**: Veri analizi ve görselleştirme için kullanıldı.
- **SQL**: Veritabanı sorguları ve veri düzenleme işlemleri için kullanıldı. Tüm veri `db.sql` dosyasında saklanmıştır.
- **Matplotlib & Seaborn**: Grafik oluşturma ve görselleştirme.
- **Pandas**: Veri işleme ve analitik operasyonlar.
- **NumPy**: Sayısal işlemler ve veri manipülasyonu.
- **MySQL**: Veritabanı yönetimi.

## Veri Kaynağı
Veriler, İzmir Büyükşehir Belediyesi'nin resmi web sitesinden günlük olarak alınmıştır. Veri seti şunları içermektedir:
- Ürün adı ve kategorisi
- Günlük minimum ve maksimum fiyatlar
- Ürün menşei (yerli/ithal)
- Birim fiyat bilgisi
- Tarih bilgisi

## Analizler ve Grafikler

### 1. Yıllık Analizler

#### 2022 Yılı Analizleri
- **En Düşük Fiyatlı Ürün Analizi**: 2022 yılı içindeki en düşük fiyata sahip ürünün fiyat değişim grafiği
  - Günlük fiyat değişimleri
  - Aylık ortalama fiyatlar
  - En düşük ve en yüksek fiyat noktaları

- **En Yüksek Fiyatlı Ürün Analizi**: 2022 yılı içindeki en yüksek fiyata sahip ürünün fiyat değişim grafiği
  - Fiyat zirve noktaları
  - Fiyat düşüş dönemleri
  - Trend analizi

- **Fiyat Artışı Yapan Ürünler**: 2022 yılında fiyat artışı yapan ürünlerin analizi
  - Artış oranlarına göre sıralama
  - Kategorilere göre artış dağılımı
  - Mevsimsel artış analizi

- **Can Eriği Fiyat Analizi**: Meyve kategorisindeki en yüksek fiyatlı ürün olan can eriğinin fiyat değişimi
  - Sezonluk fiyat değişimleri
  - Piyasaya giriş-çıkış dönemleri
  - Fiyat dalgalanmaları

- **Mantar Fiyat Analizi**: Sebze kategorisindeki en yüksek fiyatlı ürün olan mantarın fiyat değişimi
  - Günlük fiyat değişimleri
  - Üretim dönemlerine göre analiz
  - Fiyat istikrar analizi

#### 2023 Yılı Analizleri
- **En Düşük/Yüksek Fiyat Analizleri**: 2023 yılındaki en düşük ve en yüksek fiyatlı ürünlerin analizi
  - Ürün bazında karşılaştırmalar
  - Fiyat aralıkları analizi
  - Dönemsel değişimler

- **Çilek Fiyat Analizi**: Meyve kategorisinde en yüksek fiyata sahip çileğin fiyat değişimi
  - Sezon içi fiyat hareketleri
  - Üretim bölgelerine göre fiyat farklılıkları
  - İthal-yerli fiyat karşılaştırması

- **Mantar Fiyat Analizi**: Sebze kategorisinde en yüksek fiyata sahip mantarın fiyat değişimi
  - Yıl içi fiyat trendi
  - Üretim maliyetleri etkisi
  - Pazar dinamikleri analizi

#### 2024 Yılı Analizleri
- **Fiyat Değişimi En Yüksek 5 Ürün**: 2024 yılında en çok fiyat değişimi gösteren ürünlerin analizi
  - Değişim oranları
  - Değişim nedenleri
  - Kategori bazlı değerlendirme

- **En Az Fiyat Değişimi**: 2024 yılında en az fiyat değişimine sahip ilk 5 ürün
  - Stabilite analizi
  - Fiyat koruma nedenleri
  - Pazar dinamikleri

- **Yerli-İthal Karşılaştırmaları**: 
  - **Sarımsak**: Yerli ve ithal sarımsak fiyatlarının karşılaştırmalı analizi
  - **Biber**: Yerli ve ithal biber çeşitlerinin fiyat karşılaştırması
  - **Elma**: Yerli ve ithal elma fiyatlarının karşılaştırmalı analizi
  - **Kivi**: Yerli ve ithal kivi fiyatlarının dönemsel karşılaştırması
  - **Muz**: Yerli ve ithal muz fiyatlarının detaylı karşılaştırması

### 2. Mevsimsel Analizler

#### 2022 Mevsimsel Analizler
- **İlkbahar Analizi**: İlkbahar mevsiminde fiyat değişimi en yüksek olan ilk 5 ürün
  - Mart-Nisan-Mayıs ayları fiyat değişimleri
  - Sezon başlangıç etkisi
  - Üretim döngüsü analizi

- **Yaz Analizi**: Yaz mevsiminde fiyat değişimi en yüksek olan 5 ürün
  - Haziran-Temmuz-Ağustos ayları değişimleri
  - Sıcaklık etkisi analizi
  - Turizm sezonu etkisi

- **Sonbahar Analizi**: Sonbahar mevsiminde fiyat değişimi en yüksek olan ilk 5 ürün
  - Eylül-Ekim-Kasım ayları değişimleri
  - Hasat dönemi etkisi
  - Depolama etkisi

- **Kış Analizi**: Kış mevsiminde fiyat değişimi en yüksek olan ilk 5 ürün
  - Aralık-Ocak-Şubat ayları değişimleri
  - Soğuk hava etkisi
  - Sera ürünleri analizi

#### 2023 Mevsimsel Analizler
[2022 yılı ile aynı başlıklar altında detaylı analizler]

#### 2024 Mevsimsel Analizler
[2022 yılı ile aynı başlıklar altında detaylı analizler]
- **Sezon Bazında Meyve Fiyatları**: Tüm meyvelerin sezonluk fiyat değişimleri
- **Sezon Bazında Sebze Fiyatları**: Tüm sebzelerin sezonluk fiyat değişimleri

### 3. Özel Analizler

#### Fiyat Artış Analizleri
- **Meyve Türleri**: %100'ün üzerinde fiyat artışı gösteren meyve türlerinin analizi
  - Artış nedenleri
  - Artış dönemleri
  - Etki analizi

- **Sebze Türleri**: %100'ün üzerinde fiyat artışı gösteren sebze türlerinin analizi
  - Kategorik artış analizi
  - Dönemsel etkiler
  - Maliyet analizi

- **İthal Ürünler**: %100'ün üzerinde fiyat artışı gösteren ithal ürünlerin analizi
  - Döviz kuru etkisi
  - İthalat politikaları etkisi
  - Küresel pazar analizi

#### Karşılaştırmalı Analizler
- **Meyve Karşılaştırması**: 2022, 2023 ve 2024 yıllarında en yüksek fiyata sahip meyvelerin karşılaştırması
- **Sebze Minimum Fiyat**: 2022, 2023 ve 2024 yıllarında en düşük fiyata sahip sebzelerin karşılaştırması
- **Sebze Maksimum Fiyat**: 2022, 2023 ve 2024 yıllarında en yüksek fiyata sahip sebzelerin karşılaştırması

## Veri Analiz Metodolojisi
1. **Veri Toplama**
   - Günlük veri çekme
   - Veri doğrulama
   - Veri temizleme

2. **Veri İşleme**
   - Kategorilendirme
   - Normalizasyon
   - Eksik veri tamamlama

3. **Analiz Yöntemleri**
   - Zaman serisi analizi
   - İstatistiksel analiz
   - Karşılaştırmalı analiz

## Çıktılar
Tüm analizlerin grafikleri `outputs` klasöründe `.png` formatında saklanmaktadır. Her bir analiz için ayrı bir Python scripti `scripts` klasöründe bulunmaktadır.

### Grafik Formatları
- Çizgi grafikleri: Zaman serisi analizleri için
- Sütun grafikleri: Karşılaştırmalı analizler için
- Kutu grafikleri: Dağılım analizleri için
- Isı haritaları: Korelasyon analizleri için

## Teknik Gereksinimler
- Python 3.8 veya üzeri
- MySQL 8.0 veya üzeri
- Gerekli Python paketleri:
  - pandas>=1.3.0
  - numpy>=1.20.0
  - matplotlib>=3.4.0
  - seaborn>=0.11.0
  - mysql-connector-python>=8.0.0

## Nasıl Çalıştırılır?
1. Gerekli Python paketlerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```
2. Veritabanı bağlantısını `pymysqldbconnet.py` dosyasında yapılandırın
3. Tüm analizleri çalıştırmak için:
   ```bash
   python scripts/run_all.py
   ```
4. Tek bir analiz için:
   ```bash
   python scripts/[analiz_dosyası].py
   ```

## Veritabanı Yapılandırması
1. MySQL veritabanı oluşturun
2. Şema ve tabloları oluşturun:
   ```sql
   source db.sql
   ```
3. Bağlantı bilgilerini yapılandırın

## Katkıda Bulunma
Bu proje açık kaynaklıdır ve katkılarınıza açıktır. Katkıda bulunmak için:

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun
3. Değişikliklerinizi commit edin
4. Branch'inizi push edin
5. Pull request oluşturun

### Kod Standartları
- PEP 8 standartlarına uyun
- Docstring kullanın
- Birim testleri ekleyin
- Açıklayıcı commit mesajları yazın

## Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## İletişim
- Proje sorumlusu: [İsim]
- E-posta: [E-posta adresi]
- GitHub: [GitHub profili]

## Teşekkürler
- İzmir Büyükşehir Belediyesi
- Veri sağlayıcıları
- Katkıda bulunan geliştiriciler