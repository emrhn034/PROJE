import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import getpass

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def decrypt_file(encrypted_path: str, password: str):
    with open(encrypted_path, 'rb') as f:
        data = f.read()
    
    salt = data[:16]
    iv = data[16:32]
    ciphertext = data[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()

    output_path = encrypted_path.replace(".enc", ".decrypted")
    with open(output_path, 'wb') as f:
        f.write(decrypted)

    print(f"[+] Dosya çözüldü: {output_path}")

def main():
    print("AES Dosya Şifreleyici - Çözme")
    encrypted_path = input("Şifreli dosya yolunu girin (.enc): ")
    if not os.path.exists(encrypted_path):
        print("[-] Dosya bulunamadı.")
        return
    password = getpass.getpass("Parolayı girin: ")
    decrypt_file(encrypted_path, password)

if __name__ == "__main__":
    main()
