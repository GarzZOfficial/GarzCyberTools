#!/usr/bin/env python3
# Garz Cyber Tools - Ultimate Edition
# Author: Garz Cyber Security

import os
import sys
import time
import platform
from modules.hasher import HashTools
from modules.encoder import EncoderTools
from modules.password_checker import PasswordTools
from modules.crypto_tools import CryptoTools
from modules.network_tools import NetworkTools
from modules.osint_tools import OsintTools

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def banner():
    print("""
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   🔥  GARZ CYBER TOOLS v2.0 - ULTIMATE EDITION  🔥      ║
    ║                                                          ║
    ║   [*] Password Cracker    [*] Hash Generator           ║
    ║   [*] Encoder/Decoder      [*] Network Scanner         ║
    ║   [*] OSINT Tools          [*] Crypto Tools            ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """)

def main_menu():
    while True:
        clear_screen()
        banner()
        print("""
    📌 MAIN MENU:
    ═══════════════════════════════════════════════
    
    [1]  🔐 HASH GENERATOR & CRACKER
    [2]  📝 ENCODE / DECODE (Base64, Hex, ROT13, URL, Binary)
    [3]  🔒 PASSWORD STRENGTH CHECKER
    [4]  🗝️  CRYPTOGRAPHY TOOLS (AES, Caesar, XOR)
    [5]  🌐 NETWORK TOOLS (Port Scanner, Ping Sweep)
    [6]  🕵️  OSINT TOOLS (IP Info, DNS Lookup, WHOIS)
    [7]  💣 PASSWORD CRACKER (Brute Force + Wordlist)
    [8]  🛠️  UTILITIES (Text Analyzer, Password Generator)
    [9]  🚪 EXIT
    
    ═══════════════════════════════════════════════
        """)
        
        choice = input("⚡ Pilih menu (1-9): ")
        
        if choice == '1':
            hash_menu()
        elif choice == '2':
            encode_menu()
        elif choice == '3':
            PasswordTools.password_checker()
            input("\nTekan Enter...")
        elif choice == '4':
            crypto_menu()
        elif choice == '5':
            network_menu()
        elif choice == '6':
            osint_menu()
        elif choice == '7':
            PasswordTools.password_cracker()
            input("\nTekan Enter...")
        elif choice == '8':
            utilities_menu()
        elif choice == '9':
            print("\n👋 Terima kasih menggunakan Garz Cyber Tools!")
            sys.exit()
        else:
            print("❌ Pilihan tidak valid!")
            time.sleep(1)

def hash_menu():
    clear_screen()
    print("\n🔐 HASH GENERATOR & CRACKER\n")
    print("[1] Generate Hash (MD5, SHA1, SHA256, SHA512)")
    print("[2] Cek Hash (Crack dengan Wordlist)")
    print("[3] Hash File (MD5/SHA256)")
    print("[4] Kembali")
    
    choice = input("\nPilih: ")
    if choice == '1':
        text = input("Masukkan teks: ")
        HashTools.generate_hash(text)
    elif choice == '2':
        target_hash = input("Masukkan hash target: ")
        wordlist = input("Path wordlist (default: wordlist.txt): ") or "wordlist.txt"
        HashTools.crack_hash(target_hash, wordlist)
    elif choice == '3':
        filepath = input("Path file: ")
        HashTools.hash_file(filepath)
    input("\nTekan Enter...")

def encode_menu():
    clear_screen()
    print("\n📝 ENCODE / DECODE TOOLS\n")
    print("[1] Base64 Encode/Decode")
    print("[2] Hex Encode/Decode")
    print("[3] ROT13 Encode/Decode")
    print("[4] URL Encode/Decode")
    print("[5] Binary Encode/Decode")
    print("[6] Kembali")
    
    choice = input("\nPilih: ")
    if choice == '6':
        return
    
    text = input("Masukkan teks: ")
    
    if choice == '1':
        EncoderTools.base64_convert(text)
    elif choice == '2':
        EncoderTools.hex_convert(text)
    elif choice == '3':
        EncoderTools.rot13_convert(text)
    elif choice == '4':
        EncoderTools.url_convert(text)
    elif choice == '5':
        EncoderTools.binary_convert(text)
    else:
        print("❌ Pilihan salah!")
    
    input("\nTekan Enter...")

def crypto_menu():
    clear_screen()
    print("\n🗝️ CRYPTOGRAPHY TOOLS\n")
    print("[1] Caesar Cipher")
    print("[2] XOR Cipher")
    print("[3] AES Encrypt/Decrypt")
    print("[4] Kembali")
    
    choice = input("\nPilih: ")
    if choice == '4':
        return
    
    if choice == '1':
        text = input("Teks: ")
        shift = int(input("Shift (1-25): "))
        CryptoTools.caesar_cipher(text, shift)
    elif choice == '2':
        text = input("Teks: ")
        key = input("Key: ")
        CryptoTools.xor_cipher(text, key)
    elif choice == '3':
        text = input("Teks: ")
        key = input("Key (16/24/32 chars): ")
        CryptoTools.aes_crypto(text, key)
    else:
        print("❌ Pilihan salah!")
    
    input("\nTekan Enter...")

def network_menu():
    clear_screen()
    print("\n🌐 NETWORK TOOLS\n")
    print("[1] Port Scanner")
    print("[2] Ping Sweep")
    print("[3] GET IP Info")
    print("[4] Kembali")
    
    choice = input("\nPilih: ")
    if choice == '4':
        return
    
    if choice == '1':
        target = input("Target IP/Domain: ")
        NetworkTools.port_scanner(target)
    elif choice == '2':
        network = input("Network (contoh: 192.168.1): ")
        NetworkTools.ping_sweep(network)
    elif choice == '3':
        target = input("IP/Domain: ")
        NetworkTools.get_ip_info(target)
    else:
        print("❌ Pilihan salah!")
    
    input("\nTekan Enter...")

def osint_menu():
    clear_screen()
    print("\n🕵️ OSINT TOOLS\n")
    print("[1] DNS Lookup")
    print("[2] WHOIS Lookup")
    print("[3] Subdomain Finder")
    print("[4] Kembali")
    
    choice = input("\nPilih: ")
    if choice == '4':
        return
    
    domain = input("Domain target: ")
    
    if choice == '1':
        OsintTools.dns_lookup(domain)
    elif choice == '2':
        OsintTools.whois_lookup(domain)
    elif choice == '3':
        OsintTools.find_subdomains(domain)
    else:
        print("❌ Pilihan salah!")
    
    input("\nTekan Enter...")

def utilities_menu():
    clear_screen()
    print("\n🛠️ UTILITIES\n")
    print("[1] Text Analyzer")
    print("[2] Random Password Generator")
    print("[3] Kembali")
    
    choice = input("\nPilih: ")
    if choice == '1':
        text = input("Masukkan teks: ")
        PasswordTools.text_analyzer(text)
    elif choice == '2':
        length = int(input("Panjang password: "))
        PasswordTools.generate_password(length)
    else:
        return
    
    input("\nTekan Enter...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 Terima kasih!")
        sys.exit()
