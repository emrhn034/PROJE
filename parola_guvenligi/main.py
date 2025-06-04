from parola_uret import guclu_parola_uret
from parola_analiz import analiz_et
from hash_yonetimi import hashle, dogrula

def menu():
    print("🔐 Parola Güvenliği Aracı")
    print("1 - Güçlü parola üret")
    print("2 - Parola analiz et")
    print("3 - Parola hashle")
    print("4 - Parola doğrula")
    secim = input("Seçiminiz: ")

    if secim == "1":
        parola = guclu_parola_uret()
        print(f"🔑 Üretilen parola: {parola}")

    elif secim == "2":
        parola = input("Parolanızı girin: ")
        analiz = analiz_et(parola)
        print(f"💪 Güç Puanı: {analiz['puan']}/4")
        print(f"⏳ Tahmini kırılma süresi: {analiz['tahmini_kirma_suresi']}")
        print(f"💡 Öneriler: {', '.join(analiz['oneriler'])}")

    elif secim == "3":
        parola = input("Parola girin: ")
        hashed = hashle(parola)
        print(f"🔐 Hashlenmiş parola: {hashed.decode()}")

    elif secim == "4":
        parola = input("Parola girin: ")
        hashli = input("Hash'i girin: ").encode()
        if dogrula(parola, hashli):
            print("✅ Parola doğrulandı.")
        else:
            print("❌ Parola yanlış.")

if __name__ == "__main__":
    menu()
