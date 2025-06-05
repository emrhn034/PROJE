#🔐 AES File Encryptor

Bu proje, dosyaları güçlü bir AES şifreleme algoritması ile şifreleyip çözmek için geliştirilmiştir. Python kullanılarak yazılmıştır ve temel şifreleme/deşifre işlemleri gerçekleştirilir.

## 🧠 Amaç

Bilgisayarda bulunan önemli dosyaların güvenliğini artırmak ve yetkisiz erişimi engellemek amacıyla AES algoritması kullanılarak dosya şifreleme ve çözme işlemlerini gerçekleştiren bir uygulama geliştirmek.

## 🚀 Özellikler
- 📦 Dosya şifreleme (AES-256 CFB modu)
- 🔓 Şifreli dosyayı parola ile geri çözme
- 🔐 Parola tabanlı anahtar üretimi (PBKDF2 + Salt)

## 📂 Dosya Yapısı
AES_File_Encryptor/
├── aes_encryptor.py # Şifreleme işlemlerini gerçekleştiren betik
├── aes_decryptor.py # Şifre çözme işlemlerini gerçekleştiren betik
└── README.md 

## 🔧 Kullanım
### 📝 1. Şifreleme

```bash
python aes_encryptor.py
Şifrelemek istediğiniz dosya yolunu girin
Parolanızı belirleyin

Oluşan .enc uzantılı şifreli dosya, aynı klasöre kaydedilir

🔓 2. Şifre Çözme
python aes_decryptor.py
.enc uzantılı şifreli dosyanın yolunu girin
Parolayı girin
Orijinal içerik .decrypted uzantısıyla geri elde edilir

🛠 Kullanılan Teknolojiler
Python 3.x
cryptography kütüphanesi

Kurulum için:
pip install cryptography

📌 Notlar
Aynı parola ile aynı dosya her seferinde farklı şekilde şifrelenir (Salt + IV sayesinde).
Parolanızı unutmanız durumunda dosya çözülemez, dikkatli saklayınız.

📅 Proje Aşamaları
1	Proje planı ve gereksinimler belirlendi
2	AES ile şifreleme kodu geliştirildi
3	Şifre çözme özelliği eklendi

👨‍💻 Geliştirici
Bilgi Güvenliği Teknolojisi Öğrencisi
GitHub: https://github.com/emrhn034


--
