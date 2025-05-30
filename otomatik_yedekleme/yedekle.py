import os
import shutil
import json
import time
from datetime import datetime

# Config dosyasını yükle
base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, "config.json")

with open(config_path, "r") as f:
    config = json.load(f)

kaynak = config["kaynak_klasoru"]
hedef = config["hedef_klasoru"]

# Log fonksiyonu
def log_yaz(mesaj):
    log_klasoru = "logs"
    os.makedirs(log_klasoru, exist_ok=True)
    log_yolu = os.path.join(log_klasoru, "yedekleme.log")
    with open(log_yolu, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.now()}] {mesaj}\n")

# Yedekleme fonksiyonu
def yedekle():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    yedek_klasoru = os.path.join(hedef, f"yedek_{timestamp}")

    try:
        shutil.copytree(kaynak, yedek_klasoru)
        log_yaz(f"Yedekleme tamamlandı: {yedek_klasoru}")
        print("✅ Yedekleme başarıyla tamamlandı.")
    except Exception as e:
        log_yaz(f"HATA: {str(e)}")
        print("❌ Yedekleme sırasında hata oluştu. Ayrıntılar log dosyasında.")

# Haftada 1 kez Pazar günü saat 02:00'de yedekleme yapan döngü
def run_weekly_backup():
    while True:
        now = datetime.now()
        # Pazar günü: weekday() == 6
        if now.weekday() == 6 and now.hour == 2 and now.minute == 0:
            yedekle()
            # Aynı dakika içinde tekrar yedekleme yapmamak için 61 saniye bekle
            time.sleep(61)
        else:
            # CPU tüketimini azaltmak için kısa bekleme
            time.sleep(30)

if __name__ == "__main__":
    run_weekly_backup()
