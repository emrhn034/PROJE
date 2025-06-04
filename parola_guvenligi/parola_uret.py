import string
import secrets

def guclu_parola_uret(uzunluk=12):
    karakterler = string.ascii_letters + string.digits + string.punctuation
    parola = ''.join(secrets.choice(karakterler) for _ in range(uzunluk))
    return parola
