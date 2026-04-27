from cryptography.fernet import Fernet
import base64

class CryptoTools:
    @staticmethod
    def caesar_cipher(text, shift):
        print("\n[1] Enkripsi")
        print("[2] Dekripsi")
        choice = input("Pilih: ")
        
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = 65 if char.isupper() else 97
                if choice == '1':
                    result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
                else:
                    result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                result += char
        
        print(f"\n✅ Hasil: {result}")
    
    @staticmethod
    def xor_cipher(text, key):
        result = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
        print(f"\n✅ Hasil XOR: {result}")
        print(f"📝 Catatan: Jalankan lagi dengan hasil yang sama untuk dekripsi")
    
    @staticmethod
    def aes_crypto(text, key):
        print("\n[1] Enkripsi")
        print("[2] Dekripsi")
        choice = input("Pilih: ")
        
        try:
            # Generate key from password
            key_bytes = key.encode()[:32].ljust(32, b'0')
            fernet_key = base64.urlsafe_b64encode(key_bytes)
            cipher = Fernet(fernet_key)
            
            if choice == '1':
                encrypted = cipher.encrypt(text.encode())
                print(f"\n✅ Encrypted: {encrypted.decode()}")
            else:
                decrypted = cipher.decrypt(text.encode())
                print(f"\n✅ Decrypted: {decrypted.decode()}")
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Pastikan key panjangnya 16, 24, atau 32 karakter!")
