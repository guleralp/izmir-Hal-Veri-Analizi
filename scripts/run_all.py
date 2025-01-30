import os
import subprocess
from concurrent.futures import ThreadPoolExecutor
import matplotlib
matplotlib.use('Agg')  # Görsel arayüz kullanımını devre dışı bırak

def run_script(script_path):
    """Belirtilen Python scriptini çalıştırır ve sonucu yazdırır."""
    try:
        print(f"Çalıştırılıyor: {script_path}")
        # PYTHONPATH'i ayarla ve matplotlib backend'ini Agg olarak belirle
        env = os.environ.copy()
        env['MPLBACKEND'] = 'Agg'
        
        result = subprocess.run(['python', script_path], 
                              capture_output=True,
                              text=True,
                              env=env)
        
        if result.returncode == 0:
            print(f"✓ Başarıyla tamamlandı: {script_path}")
        else:
            print(f"✗ Hata oluştu ({script_path}):")
            print(result.stderr)
            
    except Exception as e:
        print(f"✗ Çalıştırma hatası ({script_path}): {str(e)}")

def main():
    # Mevcut dizini al
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Dizindeki tüm .py uzantılı dosyaları bul
    python_files = [f for f in os.listdir(current_dir) 
                   if f.endswith('.py') and f != os.path.basename(__file__)]
    
    print(f"Toplam {len(python_files)} script bulundu.")
    
    # ThreadPoolExecutor ile scriptleri paralel olarak çalıştır
    with ThreadPoolExecutor(max_workers=4) as executor:
        script_paths = [os.path.join(current_dir, f) for f in python_files]
        executor.map(run_script, script_paths)

if __name__ == "__main__":
    main()
