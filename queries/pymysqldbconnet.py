import pymysql

# MySQL bağlantı fonksiyonu
def get_db_connection():
    db_config = {
        "host": "localhost",         # MySQL sunucu adresi
        "user": "root",              # MySQL kullanıcı adı
        "password": "0619",          # MySQL şifresi
        "database": "worksheet1",    # Veritabanı adı
        "port": 3306                 # MySQL portu
    }

    connection = pymysql.connect(**db_config)
    return connection
