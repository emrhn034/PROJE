# ROADMAP.MD: SecureKit – Güvenlik Odaklı Araç Seti

## Proje Özeti  
SecureKit, bireysel ve kurumsal kullanıcılar için dört temel güvenlik aracını bir araya getiren bir Python uygulama setidir.  
- **AES_File_Encryptor**: Dosyaları AES (CBC modu) kullanarak şifreler ve çözer.  
- **Vigenère Şifreleme**: Klasik Vigenère algoritması ile metin bazlı şifreleme ve şifre çözme yapar.  
- **parola_guvenligi**: Girilen parolaların karmaşıklığını analiz eder, zayıf parolaları tespit eder ve iyileştirme önerileri sunar.  
- **otomatik_yedekleme**: Belirlenen klasörleri düzenli aralıklarla otomatik olarak yedekler.  

Her modül bağımsız çalışacak şekilde modüler bir yapıda geliştirilmiş olup, hem komut satırı (CLI) arayüzü hem de gerektiğinde eklenebilecek GUI/taslak yapılar için altyapı sağlar. Proje boyunca kodlar Git ile versiyon kontrolünde tutulacak, her aşamada testler ve dökümantasyon adımları eksiksiz tamamlanacaktır.

---

**Toplam Süre:** 5 gün  
**Geliştirici Ekibi:**  
- Emirhan Aktaş (AES_File_Encryptor, otomatik_yedekleme)  
- Yusuf Çiftçi (parola_guvenligi, Vigenère Şifreleme)  

---

## 🗓️ Gün 1: AES_File_Encryptor Modülü  
**Amaç:** Projenin temelini oluşturan AES şifreleme/çözme işlevlerini eksiksiz ve güvenli bir şekilde hayata geçirmek.  

- `pycryptodome` bağımlılığının kurulumu ve proje dizinine eklenmesi.  
- AES CBC modunda çalışan `encrypt_file(path, key, iv)` ve `decrypt_file(path, key, iv)` fonksiyonlarının yazılması.  
  - Anahtar (256-bit) ve IV üretimi için yardımcı fonksiyon (`generate_key_iv()`) geliştirme.  
  - Şifreleme sırasında dosya okuma/yazma akışının (stream) doğru çalıştığının test edilmesi.  
- Hata yönetimi ve dosya boyutu sınırları için temel kontrollerin eklenmesi (örneğin: geçersiz dosya yolu, yanlış anahtar/IV uzunluğu).  
- Çıktı olarak `.enc` uzantılı şifreli dosyanın oluşturulması ve orijinal dosyadan ayırt edilebilecek bir format belirleme.  
- Birim testler (unit test) ile AES işlevlerinin davranışlarının doğrulanması.  

---

## 🗓️ Gün 2: Vigenère Şifreleme Modülü  
**Amaç:** Klasik Vigenère algoritmasını kullanarak metin bazlı şifreleme/çözme işlevlerini tamamlamak.  

- `Vigenere Şifreleme/` klasörü altında:  
  - `vigenere.py` dosyasının oluşturulması.  
  - `vigenere_encrypt(plaintext: str, key: str) -> str` ve `vigenere_decrypt(ciphertext: str, key: str) -> str` fonksiyonlarını yazma.  
    - Küçük/büyük harf ayrımını ve sadece A–Z aralığında işlem yapmayı sağlamak.  
    - Anahtar uzunluğuna göre metni döngüsel olarak işleme mantığını uygulama.  
- Kullanıcıdan terminal üzerinden “şifrelemek/çözmek istediği metni” ve “anahtar”ı alacak basit bir CLI arayüzü ekleme.  
  - Örnek komut:  
    ```bash
    python vigenere.py --mode encrypt --key "ANAHTAR" --text "Gizli Mesaj"
    ```  
- Hata ve sınır kontrolleri ekleme:  
  - Anahtarın yalnızca alfabetik karakterlerden oluştuğunu doğrulama.  
  - Metin veya anahtar boş bırakıldığında kullanıcıyı uyarmak.  
- Kısa bir test seti ile `vigenere_encrypt`/`decrypt` fonksiyonlarının doğru çalıştığının doğrulanması.  

---

## 🗓️ Gün 3: parola_guvenligi (Parola Güvenliği Analiz Aracı)  
**Amaç:** Kullanıcıların girdikleri parolaların gücünü ölçmek, zayıf parolaları tespit etmek ve geliştirme önerileri sunmak.  

- `parola_guvenligi/` klasörü altında:  
  - `password_strength.py` dosyasının oluşturulması.  
  - `analyze_password(password: str) -> dict` fonksiyonunun yazılması; analiz sonuçlarında:  
    - Uzunluk (karakter sayısı)  
    - Büyük harf, küçük harf, rakam ve özel karakter içeriği  
    - Yaygın parola listeleriyle karşılaştırma (örn. “123456”, “password” gibi temel zayıf parolalar)  
    - Toplam puan (ör. 0–100 arası) ve metin tabanlı geri bildirim (ör. “Parolanız zayıf, en az 8 karakter, rakam ve simge ekleyin.”)  
- CLI arayüzü ekleme:  
  - Örnek komut:  
    ```bash
    python password_strength.py --password "Sifre123!"
    ```  
  - Analiz sonuçlarını JSON veya kullanıcı dostu metin formatında terminalde gösterme.  
- Birim testler ile analiz fonksiyonunun çeşitli örnek parolalar için tutarlı sonuç üretmesini doğrulama.  
- Gerektiğinde `common_passwords.txt` gibi bir dosya ile yaygın parolaları listeleyip kontrol mekanizmasını iyileştirme.  

---

## 🗓️ Gün 4: otomatik_yedekleme (Otomatik Dosya Yedekleme Sistemi)  
**Amaç:** Belirlenen klasörleri kullanıcının tanımladığı aralıklarla otomatik olarak yedekleyecek bir sistem geliştirmek.  

- `otomatik_yedekleme/` klasöründe:  
  - `backup.py` dosyasının oluşturulması.  
  - `start_backup(source_dir: str, dest_dir: str, interval: int)` fonksiyonunu yazma:  
    - `source_dir` içindeki tüm dosya/alt klasör yapısını okuyup `dest_dir` altında zaman damgalı klasör ile kopyalama.  
    - `interval` parametresiyle yedekleme aralığını saniye cinsinden ayarlama.  
  - Basit CLI arayüzü:  
    ```bash
    python backup.py --source "/home/user/dosyalar" --dest "/home/user/backup" --interval 60
    ```  
    - Kullanıcı aralık (dakika/saniye) belirtmezse varsayılan olarak 60 saniye ayarlanacak.  
  - Dosya kopyalama sırasında:
    - Önceki yedekleme klasörünü kontrol etme, aynı dosya/dizin adı zaten varsa üzerine yazmama veya yeniden adlandırma (ör. `file_1.txt`, `file_2.txt` gibi).  
    - Hata yönetimi ekleme (örneğin: izin problemi, disk doluluğu).  
- Gerektiğinde günlük (log) tutma:  
  - `backup.log` dosyası oluşturarak her yedekleme adımını kayıt altına alma (tarih, kaynak dosya, hedef yol, işlem durumu).  
- Küçük bir test senaryosu ile 2–3 dosya/klasör yedeğini farklı zaman aralıklarında çalıştırarak doğrulama.  

---

## 🗓️ Gün 5: Entegrasyon, Test ve Dokümantasyon  
**Amaç:** Tüm modülleri aynı dizin yapısına entegre edip, eksiksiz dökümantasyon ve testlerle projeyi yayına hazır hale getirmek.  

1. **Proje Dizini Düzenlemesi ve Modüler Entegrasyon**  
   - Kök dizinde aşağıdaki klasör yapısının doğrulanması:  
     ```
     SecureKit/
     ├── AES_File_Encryptor/
     │   └── encryptor.py
     ├── Vigenere Şifreleme/
     │   └── vigenere.py
     ├── parola_guvenligi/
     │   └── password_strength.py
     ├── otomatik_yedekleme/
     │   └── backup.py
     ├── requirements.txt
     ├── README.md
     └── ROADMAP.md
     ```  
   - Gerekli bağımlılıkların `requirements.txt` içinde listelenmesi:  
     ```
     pycryptodome
     ```  
   - Tüm Python betiklerine çalıştırma izni (Linux/macOS için `chmod +x`) verilmesi.  

2. **Ortak CLI Yönetimi (Opsiyonel)**  
   - İleride merkezi bir `main.py` oluşturularak kullanıcı, komut satırından hangi aracı çalıştırmak istediğini seçebilsin:  
     ```bash
     python main.py --module aes --encrypt --input "file.txt" --key "..." --iv "..."
     python main.py --module vigenere --mode decrypt --key "ANAHTAR" --text "..."  
     python main.py --module password_strength --password "..."  
     python main.py --module backup --source "/kaynak" --dest "/yedek" --interval 120  
     ```  
   - Bu entegrasyon yapılmasa da her modül bağımsız çalışabilir.  

3. **Test Senaryoları ve Otomasyon**  
   - Her klasör altında basit birim test dosyası (`test_*.py`) ekleyerek modüllerin beklenen çıktıyı verdiğinden emin olma.  
   - Örneğin, `AES_File_Encryptor/test_encryptor.py` içinde:
     ```python
     import os
     from encryptor import encrypt_file, decrypt_file, generate_key_iv
     
     def test_aes_encrypt_decrypt(tmp_path):
         key, iv = generate_key_iv()
         original = tmp_path / "orijinal.txt"
         encrypted = tmp_path / "orijinal.txt.enc"
         decrypted = tmp_path / "orijinal_decrypted.txt"
         
         original.write_text("Gizli İçerik")
         encrypt_file(str(original), str(encrypted), key, iv)
         decrypt_file(str(encrypted), str(decrypted), key, iv)
         assert decrypted.read_text() == "Gizli İçerik"
     ```  
   - Benzer testler Vigenère, parola_guvenligi ve otomatik_yedekleme modülleri için hazırlanacak.  

4. **README.md ve Örnek Kullanımlar**  
   - Her modül için kısa kullanım örneklerini `README.md` içinde şu şekilde sun:  
     ```markdown
     ## AES_File_Encryptor
     ```bash
     # AES şifreleme
     python AES_File_Encryptor/encryptor.py --mode encrypt --input "dokuman.txt" --key "anahtar" --iv "0123456789abcdef" 
     # AES çözme
     python AES_File_Encryptor/encryptor.py --mode decrypt --input "dokuman.txt.enc" --key "anahtar" --iv "0123456789abcdef"
     ```
     
     ## Vigenère Şifreleme
     ```bash
     python "Vigenere Şifreleme"/vigenere.py --mode encrypt --key "GIZLIANAHTAR" --text "Merhaba Dünya"
     python "Vigenere Şifreleme"/vigenere.py --mode decrypt --key "GIZLIANAHTAR" --text "ŞifreliMetin"
     ```
     
     ## parola_guvenligi
     ```bash
     python parola_guvenligi/password_strength.py --password "Sifre123!"
     ```
     
     ## otomatik_yedekleme
     ```bash
     python otomatik_yedekleme/backup.py --source "/home/user/dosyalar" --dest "/home/user/backup" --interval 60
     ```  
   - Projenin genel amacı, kurulumu ve katkıda bulunma adımları eksiksiz anlatılacak.  

5. **Son Kontroller ve Yayınlama**  
   - Tüm modüller tek tek çalıştırılarak doğru çıktıyı verdiği kontrol edilecek.  
   - Gereksiz veya geçici dosyalar (`__pycache__`, `.pyc`, vs.) `.gitignore` dosyasına eklenecek.  
   - Versiyon bilgisi ve lisans (`MIT`) dosyaları gözden geçirilecek.  
   - “Release” amacına uygun bir “v1.0.0” etiketi oluşturularak GitHub’a push edilecek.  

---

> **Not:** Bu yol haritası, SecureKit’in mevcut dört ana modülüne odaklanmıştır. İlerleyen zamanlarda GUI entegrasyonu, ek şifreleme algoritmaları veya daha gelişmiş yedekleme senaryoları gibi ek özellikler planlanabilir...
