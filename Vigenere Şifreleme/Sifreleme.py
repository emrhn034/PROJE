def temizle_metin(metin):
    return ''.join(filter(str.isalpha, metin.upper()))

def vigenere_sifrele(metin, anahtar):
    metin = temizle_metin(metin)
    anahtar = temizle_metin(anahtar)
    sifreli = ''
    for i in range(len(metin)):
        harf = metin[i]
        anahtar_harfi = anahtar[i % len(anahtar)]
        sifre_harfi = chr(((ord(harf) - 65 + ord(anahtar_harfi) - 65) % 26) + 65)
        sifreli += sifre_harfi
    return sifreli

def vigenere_desifrele(sifreli, anahtar):
    sifreli = temizle_metin(sifreli)
    anahtar = temizle_metin(anahtar)
    cozulmus = ''
    for i in range(len(sifreli)):
        harf = sifreli[i]
        anahtar_harfi = anahtar[i % len(anahtar)]
        orijinal_harf = chr(((ord(harf) - ord(anahtar_harfi) + 26) % 26) + 65)
        cozulmus += orijinal_harf
    return cozulmus

if __name__ == "__main__":
    print("🔐 Vigenère Şifreleme Aracı")
    secim = input("1- Şifrele\n2- Çöz\nSeçiminiz: ")
    metin = input("Metni girin: ")
    anahtar = input("Anahtarı girin: ")

    if secim == '1':
        sifreli = vigenere_sifrele(metin, anahtar)
        print("🔒 Şifreli Metin:", sifreli)
    elif secim == '2':
        cozulmus = vigenere_desifrele(metin, anahtar)
        print("🔓 Çözülmüş Metin:", cozulmus)
    else:
        print("Hatalı seçim.")
