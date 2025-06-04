from zxcvbn import zxcvbn

def analiz_et(parola):
    sonuc = zxcvbn(parola)
    return {
        "puan": sonuc['score'],
        "tahmini_kirma_suresi": sonuc['crack_times_display']['offline_slow_hashing_1e4_per_second'],
        "oneriler": sonuc['feedback']['suggestions']
    }
