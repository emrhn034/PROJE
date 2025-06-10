<div align="center">
  <img src="https://img.shields.io/github/languages/count/emrhn034/SecureKit?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/emrhn034/SecureKit?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/emrhn034/SecureKit?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/emrhn034/SecureKit?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
  <img src="https://img.shields.io/github/MIT/emrhn034/SecureKit?style=flat-square&color=ff69b4" alt="MIT">
</div>

🛡️ SecureKit

📢Her modülün kendi klasöründe o modüle dair `README.md` ve ilgili dokümantasyon dosyaları bulunmaktadır. Lütfen başlamadan önce bu dosyaları mutlaka inceleyin.**

🔐Güvenlik odaklı araçlardan oluşan kapsamlı bir yazılım setidir. 
👇Bu proje kapsamında geliştirilen üç temel araç şunlardır:

🔐Vigenère algoritması, şifreleme işleminde bir anahtar kelime kullanarak metin bazlı çok alfabeli şifreleme sağlar. SecureKit içinde bu algoritma, küçük çaplı ya da eğitsel metin şifreleme senaryoları için örnek olarak eklenmiştir.

🗄️ AES_File_Encryptor: Dosyaları AES algoritması ile güçlü bir şekilde şifreler.

🧪 parola_guvenligi: Parolaların güvenlik seviyesini analiz eder, zayıf parolaları tespit eder.

📂 otomatik_yedekleme: Belirlenen klasörleri belirli aralıklarla yedekler, veri kaybına karşı koruma sağlar.

🧰 SecureKit, bu üç aracı bir araya getirerek bireysel ve kurumsal kullanıcılar için güçlü, pratik ve genişletilebilir bir güvenlik çözüm seti sunar.
---

🚀 Features / Özellikler /
🔐 AES-Based File Encryption
AES Tabanlı Dosya Şifreleme
Securely encrypts selected files using the AES (Advanced Encryption Standard) algorithm.
Seçilen dosyaları AES algoritmasıyla güvenli bir şekilde şifreler.

🔓 AES-Based File Decryption
AES Tabanlı Dosya Şifre Çözme
Decrypts previously encrypted files using the correct password.
Daha önce şifrelenmiş dosyaların doğru parola ile şifresini çözer.

💾 Automatic File Backup
Otomatik Dosya Yedekleme
Periodically backs up important files to a predefined directory.
Önemli dosyaları belirlenen bir dizine düzenli olarak yedekler.

📁 Custom Backup Path Support
Özelleştirilebilir Yedekleme Yolu Desteği
Users can specify the backup path for storing copies of original files.
Kullanıcılar yedeklerin saklanacağı dizini belirleyebilir.

⏱️ Configurable Backup Interval
Yedekleme Aralığı Ayarlanabilir
The backup system runs on a set interval (e.g., every 60 seconds).
Yedekleme sistemi belirli aralıklarla (örneğin her 60 saniyede bir) çalışır.

💻 Command-Line Interface
Komut Satırı Arayüzü
Simple CLI for selecting files, setting passwords, and initiating operations.
Dosya seçimi, parola belirleme ve işlemleri başlatmak için basit bir CLI sunar.

🔁 Password Confirmation
Parola Doğrulama
Double-entry password confirmation to reduce errors during encryption.
Şifreleme sırasında hataları azaltmak için iki kez parola girilmesi istenir.

⚙️ Lightweight & Easy to Use
Hafif ve Kullanımı Kolay
Minimal dependencies and easy-to-understand Python implementation.
Minimum bağımlılıklarla yazılmış, kolay anlaşılır Python kod yapısı.

---

👥 Team / Ekip

🧑‍💻 2320191067 - Emirhan Aktaş: Project Lead, AES Encryption & Backup System Development
Proje Lideri, AES Şifreleme ve Yedekleme Sistemi Geliştirici
github/emrhn034

👨‍💻 2320191079 - Yusuf Çiftçi: Password Security Implementation
Parola Güvenliği Uygulaması & Vigenere Şifreleme
github/Ysftcftcc

---

 *Yol Haritası*

ROADMAP.MD: SecureKit – Güvenlik Odaklı Araç Seti
[ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Aircrack Deep Dive      | [researchs/aircrack.md](researchs/aircrack.md) | In-depth analysis of Aircrack-ng suite. / *Aircrack-ng paketinin derinlemesine analizi.* |
| Example Research Topic  | [researchs/your-research-file.md](researchs/your-research-file.md) | Brief overview of this research. / *Bu araştırmanın kısa bir özeti.* |
| Add More Research       | *Link to your other research files*     | *Description of the research*                  |

---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage / *Kullanım*

Run the project:  
*Projeyi çalıştırın:*

```bash
python main.py --input your_file.pcap --output results.txt
```

**Steps**:  
1. Prepare input data (*explain data needed*).  
2. Run the script with arguments (*explain key arguments*).  
3. Check output (*explain where to find results*).  

*Adımlar*:  
1. Giriş verilerini hazırlayın (*ne tür verilere ihtiyaç duyulduğunu açıklayın*).  
2. Betiği argümanlarla çalıştırın (*önemli argümanları açıklayın*).  
3. Çıktıyı kontrol edin (*sonuçları nerede bulacağınızı açıklayın*).

---

## Contributing / *Katkıda Bulunma*

We welcome contributions from the community! Please follow the steps below to contribute:

Topluluk katkılarını memnuniyetle karşılıyoruz! Katkıda bulunmak için lütfen aşağıdaki adımları izleyin:

📌 Steps / Adımlar
🧑‍💻Kullanıcı: emrhn034

Fork the repository

Click the "Fork" button in the top-right corner of this page to create a copy under your GitHub account.

Clone your fork

Terminal veya komut satırında aşağıdaki komutu kullanarak kendi kopyanızı bilgisayarınıza indirin:

git clone git@github.com:emrhn034/emrhn034.github.io.git

Create a new branch

Yeni bir özellik geliştirmek veya hata düzeltmek için yeni bir dal oluşturun:

git checkout -b feature/your-feature

Make changes and commit

Gerekli değişiklikleri yapın ve anlamlı commit mesajlarıyla kaydedin:

git commit -m "SecurityKit"

Push your changes

Değişikliklerinizi kendi fork’unuza gönderin

git push origin feature/your-feature

🧑‍💻Kullanıcı: ysftcftcc
Fork the repository

Click the "Fork" button in the top-right corner of this page to create a copy under your GitHub account.

Clone your fork

Terminal veya komut satırında aşağıdaki komutu kullanarak kendi kopyanızı bilgisayarınıza indirin:

git clone git@github.com:ysftcftcc/ysftcftcc.github.io.git

Create a new branch

Yeni bir özellik geliştirmek veya hata düzeltmek için yeni bir dal oluşturun:

git checkout -b feature/your-feature

Make changes and commit

Gerekli değişiklikleri yapın ve anlamlı commit mesajlarıyla kaydedin:

git commit -m "SecurityKit"

Push your changes

Değişikliklerinizi kendi fork’unuza gönderin

git push origin feature/your-feature



---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler* (Optional)

Thanks to:  
- Awesome Library: For enabling X.  
- Inspiration Source.  
- Special thanks to...  

*Teşekkürler: Harika kütüphaneler ve ilham kaynakları için.*

---

## Contact / *İletişim* (Optional)

Project Maintainer: [Your Name/Org Name] - [your.email@example.com]  
Found a bug? Open an issue.  

*Proje Sorumlusu: [Adınız/Kuruluş Adınız] - [e-posta.adresiniz@ornek.com]. Hata bulursanız bir sorun bildirin.*

---

*Replace placeholders (e.g., YOUR_USERNAME/YOUR_REPO) with your project details.*
