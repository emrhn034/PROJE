# aes_encryptor.py

from cryptography.fernet import Fernet

def main():
    print("AES Dosya Şifreleyici")
    # Buraya kullanıcıdan dosya yolu ve parola alma gibi işlemler eklenecek

if __name__ == "__main__":
    main()
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode
import getpass

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path: str, password: str):
    # Rastgele 16 baytlık salt ve iv üret
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        plaintext = f.read()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    encrypted_path = file_path + ".enc"
    with open(encrypted_path, 'wb') as f:
        # Başta salt + iv + şifreli veri yaz
        f.write(salt + iv + ciphertext)

    print(f"[+] Dosya şifrelendi: {encrypted_path}")

def main():
    print("AES Dosya Şifreleyici - Şifreleme")
    file_path = input("Şifrelenecek dosyanın yolunu girin: ")
    if not os.path.exists(file_path):
        print("[-] Dosya bulunamadı.")
        return
    password = getpass.getpass("Parola girin: ")
    encrypt_file(file_path, password)

if __name__ == "__main__":
    main()
