#!/usr/bin/env python3
# Garz Cyber Tools - Hash Generator, Encode/Decode, Password Checker

import hashlib
import base64
import sys

def banner():
    print("""
    🔥 GARZ CYBER TOOLS v1.0 🔥
    [1] Hash Generator (MD5, SHA1, SHA256)
    [2] Encode / Decode (Base64)
    [3] Password Strength Checker
    [4] Exit
    """)

def hash_generator():
    text = input("\n📝 Masukkan teks: ")
    print(f"\nMD5     : {hashlib.md5(text.encode()).hexdigest()}")
    print(f"SHA1    : {hashlib.sha1(text.encode()).hexdigest()}")
    print(f"SHA256  : {hashlib.sha256(text.encode()).hexdigest()}")

def encode_decode():
    print("\n[1] Encode ke Base64")
    print("[2] Decode dari Base64")
    choice = input("Pilih (1/2): ")
    
    if choice == '1':
        text = input("Teks: ")
        result = base64.b64encode(text.encode()).decode()
        print(f"✅ Hasil Encode: {result}")
    elif choice == '2':
        b64_text = input("Base64: ")
        try:
            result = base64.b64decode(b64_text).decode()
            print(f"✅ Hasil Decode: {result}")
        except:
            print("❌ Base64 tidak valid!")
    else:
        print("❌ Pilihan salah!")

def password_checker():
    pwd = input("\n🔐 Masukkan password: ")
    length = len(pwd)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_special = any(not c.isalnum() for c in pwd)
    
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    
    print("\n🔍 Analisis:")
    print(f"Panjang      : {length} karakter")
    print(f"Huruf besar  : {'✔️' if has_upper else '❌'}")
    print(f"Huruf kecil  : {'✔️' if has_lower else '❌'}")
    print(f"Angka        : {'✔️' if has_digit else '❌'}")
    print(f"Karakter khusus : {'✔️' if has_special else '❌'}")
    
    if score <= 2:
        strength = "LEMAH ❌"
    elif score == 3 or score == 4:
        strength = "SEDANG ⚠️"
    else:
        strength = "KUAT ✅"
    
    print(f"\n💪 Kekuatan Password: {strength}")

def main():
    while True:
        banner()
        choice = input("⚡ Pilih menu (1-4): ")
        if choice == '1':
            hash_generator()
        elif choice == '2':
            encode_decode()
        elif choice == '3':
            password_checker()
        elif choice == '4':
            print("👋 Terima kasih telah menggunakan Garz Cyber Tools!")
            sys.exit()
        else:
            print("❌ Menu tidak tersedia!")
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
