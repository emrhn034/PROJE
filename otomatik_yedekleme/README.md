# 📦 Otomatik Yedekleme Scripti

## 🎯 Amaç
Bu proje, belirlediğiniz bir kaynak klasörü haftada bir kez otomatik olarak tam yedekleyen, yedekleri zaman damgasıyla hedef klasör içinde saklayan ve işlemlerle ilgili log tutan basit bir Python tabanlı yedekleme sistemidir.

---
## ✨ Özellikler
- 📂 **Tam Yedekleme:** Kaynak klasördeki tüm dosya ve klasörler hedefe kopyalanır.
- ⏰ **Haftalık Otomatik Yedekleme:** Script, Pazar günleri saat 02:00'de yedekleme yapacak şekilde tasarlanmıştır. İsterseniz Bunu Kolayca Degiştirebilirsiniz.
- 💾 **Sürekli Saklama:** Önceki yedekler silinmez, her yedek farklı klasörde saklanır.
- 📝 **Loglama:** Yedekleme işlemi ve olası hatalar `logs/yedekleme.log` dosyasına kaydedilir.
- ⚙️ **Kolay Konfigürasyon:** Kaynak ve hedef klasörler `config.json` dosyasından ayarlanabilir.
- 🚀 **Basit Kullanım:** Python bilgisi olan herkes kolayca kullanabilir.

---
## 📁 Dosya Yapısı
otomatik_yedekleme/
│
├── yedekle.py # Ana yedekleme scripti
├── config.json # Kaynak ve hedef klasör ayarları
├── logs/ # Log dosyalarının bulunduğu klasör (otomatik oluşturulur)
│ └── yedekleme.log # Yedekleme log dosyası
└── README.md # Proje hakkında bilgiler

---

## 🚀 Kurulum ve Kullanım
### 🛠️ Gereksinimler
- Python 3.x
- İşletim sistemine göre Python'un `shutil`, `json` gibi standart kütüphaneleri yeterlidir.

### 📝 Adımlar
1. 📥 Bu depoyu klonlayın veya indirin.
2. ⚙️ `config.json` dosyasını açın ve aşağıdaki örneğe göre kaynak ve hedef klasör yollarınızı düzenleyin:

```json
{
  "kaynak_klasoru": "C:/Kullanici/Dosyalar/KaynakKlasor",
  "hedef_klasoru": "D:/Yedekler"
}
💻 Komut satırında proje klasörüne gidin.

▶️ Scripti çalıştırın:
python yedekle.py
❗ Not: Script sürekli açık kalmalıdır; haftada bir kez Pazar günü saat 02:00’de otomatik olarak yedekleme yapacaktır.

🛑 Scripti Durdurmak
Çalışan scripti durdurmak için terminalde Ctrl + C tuş kombinasyonunu kullanabilirsiniz.

💡 Öneriler
🔄 Script'in sürekli çalışmasını sağlamak için bir sunucu veya sürekli açık olan bir bilgisayar tercih edin.

🕒 Daha profesyonel bir kullanım için işletim sistemi zamanlayıcıları (cron, Windows Görev Zamanlayıcı) ile scripti periyodik olarak çalıştırabilirsiniz.

🗃️ Log dosyalarının boyutunu kontrol etmek ve eski logları arşivlemek için ek fonksiyonlar ekleyebilirsiniz.

📈 Yedekleme işlemini daha esnek yapmak için tam veya artımlı yedekleme seçenekleri eklenebilir.