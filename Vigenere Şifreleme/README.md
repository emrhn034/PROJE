# 🔐 Vigenère Şifreleme Aracı (Python)

Bu proje, klasik bir şifreleme algoritması olan **Vigenère Cipher**'ı kullanarak metinleri şifreleyen ve çözebilen bir terminal uygulamasıdır. Basit ve öğretici bir örnek olarak siber güvenlik projelerinde veya kriptografi derslerinde kullanılabilir.

---

## 📌 Özellikler

- Metinleri **Vigenère algoritmasıyla şifreler**.
- Verilen anahtar ile **şifrelenmiş metni çözer**.
- Sadece harf karakterleri ile çalışır (boşluk ve noktalama işaretleri yok sayılır).
- Büyük/küçük harf duyarsızdır.

---

## 🚀 Kurulum

> Python 3 yüklü olmalıdır.

1. Bu repoyu klonlayın veya dosyayı indirin:

```bash
git clone https://github.com/kullanici-adi/vigenere-sifreleme-araci.git
cd vigenere-sifreleme-araci

python vigenere.py

🔐 Vigenère Şifreleme Aracı
1- Şifrele
2- Çöz
Seçiminiz:

Metni girin: Merhaba Dünya
Anahtarı girin: ANAHTAR
🔒 Şifreli Metin: MNBNHBPTRFFR

vigenere-sifreleme-araci/
├── vigenere.py       # Ana Python dosyası
└── README.md         # Proje açıklaması

Vigenère şifrelemesi, her harfi anahtardaki karşılık gelen harf kadar kaydırarak şifreleme yapan bir polialfabetik şifreleme yöntemidir. Caesar algoritmasının tekrarlı anahtarla yapılan versiyonudur ve tarihsel olarak uzun yıllar kırılması zor bir yöntem olarak kullanılmıştır.

Geliştirici  Ysftcftcc


