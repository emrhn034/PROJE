# 🔐 Parola Güvenliği Aracı (Password Security Tool)

Bu Python tabanlı araç, kullanıcıların güçlü parolalar üretmesini, mevcut parolaların güvenliğini analiz etmesini ve parolaları güvenli biçimde saklamasını sağlar.

---
## 🎯 Amaç

- 🔒 Kullanıcıların parolalarını güvenli hale getirmek
- 🔑 Rastgele güçlü şifreler üretmek
- 🧠 Mevcut şifrelerin gücünü analiz etmek
- 🧂 Güvenli hash algoritmaları ile şifre saklamak
---

## ✨ Özellikler
- 🔢 Güçlü parola üretimi (secrets + string)
- 📊 Parola analiz (zxcvbn ile tahmini kırılma süresi ve öneriler)
- 🔐 `bcrypt` ile hashleme ve doğrulama
- 💡 Basit terminal menüsü ile kolay kullanım
- ⚙️ Modüler dosya yapısı

---
## 📁 Dosya Yapısı

parola_guvenligi/
├── main.py # Ana menü ve kullanıcı arayüzü
├── parola_analiz.py # Parola güç analizi
├── parola_uret.py # Parola üretimi
├── hash_yonetimi.py # Hashleme ve doğrulama
├── requirements.txt # Gerekli kütüphaneler
└── README.md # Bu dosya
---

## ▶️ Nasıl Kullanılır?
### 1️⃣ Adım: Kütüphaneleri Kur
---
pip install -r requirements.txt
2️⃣ Adım: Uygulamayı Başlat
python main.py
3️⃣ Adım: Menüden Seçim Yap
Aşağıdaki gibi bir menü açılacaktır:

🔐 Parola Güvenliği Aracı
1 - Güçlü parola üret
2 - Parola analiz et
3 - Parola hashle
4 - Parola doğrula
Seçiminiz:
🔁 Örnek Kullanımlar
🔑 Güçlü Parola Üret
Seçiminiz: 1
🔑 Üretilen parola: kP8!rA@7$zF

🧪 Parola Analiz Et
Seçiminiz: 2
Parolanızı girin: 123456
💪 Güç Puanı: 0/4
⏳ Tahmini kırılma süresi: instant
💡 Öneriler: Add another word or two. Uncommon words are better.

🧬 Parola Hashle
Seçiminiz: 3
Parola girin: gucluParola123!
🔐 Hashlenmiş parola: $2b$12$Wb8...

🔁 Parola Doğrula
Seçiminiz: 4
Parola girin: gucluParola123!
Hash'i girin: $2b$12$Wb8...
✅ Parola doğrulandı.

🛠️ Gereksinimler
Python 3.7+
bcrypt, zxcvbn

Kurulum:
pip install bcrypt zxcvbn
Ya da:
pip install -r requirements.txt
🔐 Güvenlik Notları
Bu uygulama temel amaçlıdır. Gerçek sistemlerde parola yönetimi için ilave güvenlik önlemleri gerekir.




👨‍💻 Geliştirici
Bilgi Güvenliği Teknolojisi Öğrencisi
GitHub: https://github.com/emrhn034

👨‍💻 Geliştirici
Bilgi Güvenliği Teknolojisi Öğrencisi
https://github.com/Ysftcftcc
--
