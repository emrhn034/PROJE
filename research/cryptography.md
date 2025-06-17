Kriptografi Temelleri
Bu doküman, kriptografinin temel kavramlarını ve güvenlikteki uygulamalarını tanıtmaktadır. Kriptografi, verilerin gizliliğini, bütünlüğünü ve kimlik doğrulamasını sağlamak için kullanılan bir dizi teknik ve algoritmadır.
İçindekiler

Giriş
Temel Kavramlar
Şifreleme ve Deşifreleme
Anahtarlar
Algoritmalar


Simetrik Kriptografi
AES (Advanced Encryption Standard)
DES (Data Encryption Standard)


Asimetrik Kriptografi
RSA (Rivest-Shamir-Adleman)
ECC (Elliptic Curve Cryptography)


Kullanım Alanları
Veri Güvenliği
Dijital İmzalar


En İyi Uygulamalar
Anahtar Yönetimi
Güçlü Algoritmalar Seçimi


Sonuç

Giriş
Kriptografi, verilerin yetkisiz erişime karşı korunmasını sağlayan matematiksel tekniklerin bütünüdür. Günümüzde, internet üzerinden yapılan iletişimlerin ve depolanan verilerin güvenliği için vazgeçilmezdir. Kriptografi, gizlilik, bütünlük, kimlik doğrulama ve inkâr edilemezlik gibi temel güvenlik hizmetlerini sağlar.
Temel Kavramlar
Şifreleme ve Deşifreleme

Şifreleme: Açık metni (plaintext) şifreli metne (ciphertext) dönüştürme işlemidir. Bu işlem, verilerin gizliliğini sağlar.
Deşifreleme: Şifreli metni tekrar açık metne dönüştürme işlemidir. Bu işlem, yalnızca yetkili kişiler tarafından yapılabilir.

Anahtarlar

Simetrik Anahtar: Hem şifreleme hem de deşifreleme için aynı anahtarın kullanıldığı sistemlerde kullanılır.
Asimetrik Anahtarlar: Şifreleme ve deşifreleme için farklı anahtarların (genellikle bir genel ve bir özel anahtar) kullanıldığı sistemlerde kullanılır.

Algoritmalar

Şifreleme Algoritmaları: Verileri şifrelemek ve deşifrelemek için kullanılan matematiksel prosedürlerdir. Örnekler: AES, RSA, DES.

Simetrik Kriptografi
Simetrik kriptografi, şifreleme ve deşifreleme işlemlerinde aynı anahtarın kullanıldığı yöntemdir. Bu yöntem, hızlı ve verimli olduğu için büyük veri setlerinin şifrelenmesinde tercih edilir.
AES (Advanced Encryption Standard)

Tanım: AES, 128, 192 veya 256 bit anahtar uzunluklarıyla çalışan bir blok şifreleme algoritmasıdır. Günümüzde en yaygın kullanılan şifreleme standartlarından biridir.
Nasıl Çalışır: Veri bloklarını (128 bit) anahtar ile şifreler ve deşifreler. Güvenli ve hızlıdır.

DES (Data Encryption Standard)

Tanım: DES, 56 bit anahtar kullanan eski bir şifreleme algoritmasıdır. Günümüzde güvenlik açısından yetersiz kabul edilir ve yerini AES'e bırakmıştır.
Nasıl Çalışır: 64 bitlik veri bloklarını şifreler. Brute force saldırılarına karşı savunmasızdır.

Asimetrik Kriptografi
Asimetrik kriptografi, şifreleme ve deşifreleme için farklı anahtarların kullanıldığı yöntemdir. Bu yöntem, anahtar dağıtımı sorununu çözer ve dijital imzalar gibi ek güvenlik hizmetleri sağlar.
RSA (Rivest-Shamir-Adleman)

Tanım: RSA, büyük asal sayılar ve modüler aritmetik üzerine kurulu bir asimetrik şifreleme algoritmasıdır. Genellikle anahtar değişimi ve dijital imzalar için kullanılır.
Nasıl Çalışır: Her kullanıcı bir genel ve bir özel anahtar çifti oluşturur. Genel anahtar ile şifrelenen veri, yalnızca özel anahtar ile deşifre edilebilir.

ECC (Elliptic Curve Cryptography)

Tanım: ECC, eliptik eğriler üzerindeki matematiksel problemlere dayanan bir asimetrik şifreleme yöntemidir. RSA'e göre daha küçük anahtar boyutlarıyla aynı güvenlik seviyesini sağlar.
Nasıl Çalışır: Eliptik eğriler üzerindeki nokta çarpma işlemleri kullanılarak anahtarlar oluşturulur ve şifreleme/deşifreleme yapılır.

Kullanım Alanları
Veri Güvenliği

Transit Halindeki Veriler: İnternet üzerinden gönderilen verilerin şifrelenmesi (ör. HTTPS, SSL/TLS).
Depolanan Veriler: Sabit disklerde veya bulut depolama alanlarında verilerin şifrelenmesi.

Dijital İmzalar

Tanım: Dijital imzalar, bir belgenin veya mesajın kimliğini ve bütünlüğünü doğrulamak için kullanılır.
Nasıl Çalışır: Gönderici, mesajın hash'ini özel anahtarıyla şifreler (imzalar). Alıcı, göndericinin genel anahtarıyla bu imzayı deşifre ederek doğrulama yapar.

En İyi Uygulamalar
Anahtar Yönetimi

Güvenli Anahtar Depolama: Anahtarlar, yetkisiz erişime karşı korunmalıdır (ör. HSM - Hardware Security Module).
Anahtar Rotasyonu: Belirli aralıklarla anahtarların değiştirilmesi, güvenlik risklerini azaltır.

Güçlü Algoritmalar Seçimi

Güncel Algoritmalar Kullanma: Zayıf veya eski algoritmalar yerine (ör. DES), güçlü ve güncel algoritmalar (ör. AES-256, RSA-2048) tercih edilmelidir.
Parametre Seçimi: Anahtar uzunlukları ve diğer parametreler, güvenlik gereksinimlerine uygun olmalıdır.

Sonuç
Kriptografi, modern güvenlik uygulamalarının temel taşıdır. Verilerin gizliliğini, bütünlüğünü ve kimlik doğrulamasını sağlamak için vazgeçilmezdir. Simetrik ve asimetrik kriptografi yöntemleri, farklı kullanım senaryolarına uygun çözümler sunar. Güvenli bir sistem tasarlamak için kriptografinin temel prensiplerini ve en iyi uygulamalarını bilmek önemlidir.
