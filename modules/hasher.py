import hashlib
import os

class HashTools:
    @staticmethod
    def generate_hash(text):
        print(f"\n📝 Teks: {text}")
        print(f"MD5     : {hashlib.md5(text.encode()).hexdigest()}")
        print(f"SHA1    : {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"SHA256  : {hashlib.sha256(text.encode()).hexdigest()}")
        print(f"SHA512  : {hashlib.sha512(text.encode()).hexdigest()}")
    
    @staticmethod
    def crack_hash(target_hash, wordlist):
        try:
            with open(wordlist, 'r', encoding='utf-8', errors='ignore') as f:
                words = f.readlines()
                print(f"\n🔍 Mencoba {len(words)} kata...")
                for i, word in enumerate(words):
                    word = word.strip()
                    # Cek MD5
                    if hashlib.md5(word.encode()).hexdigest() == target_hash:
                        print(f"\n✅ Hash CRACKED! Password: {word}")
                        return
                    # Cek SHA1
                    if hashlib.sha1(word.encode()).hexdigest() == target_hash:
                        print(f"\n✅ Hash CRACKED! Password: {word}")
                        return
                    # Cek SHA256
                    if hashlib.sha256(word.encode()).hexdigest() == target_hash:
                        print(f"\n✅ Hash CRACKED! Password: {word}")
                        return
                    
                    if i % 1000 == 0:
                        print(f"🔍 Progress: {i}/{len(words)} kata...", end='\r')
            print("\n❌ Password tidak ditemukan di wordlist!")
        except FileNotFoundError:
            print("❌ File wordlist tidak ditemukan!")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    @staticmethod
    def hash_file(filepath):
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
                print(f"\n📁 File: {filepath}")
                print(f"MD5    : {hashlib.md5(data).hexdigest()}")
                print(f"SHA256 : {hashlib.sha256(data).hexdigest()}")
        except FileNotFoundError:
            print("❌ File tidak ditemukan!")
