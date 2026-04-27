cat > garz_tools.py << 'EOF'
#!/usr/bin/env python3
# Garz Cyber Tools v3.0 - Termux Edition

import os
import sys
import time
import platform

def clear_screen():
    os.system('clear')

def banner():
    print("\033[91m")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║                                                                ║")
    print("║   ██████╗  █████╗ ██████╗ ███████╗                            ║")
    print("║   ██╔════╝ ██╔══██╗██╔══██╗╚══███╔╝                            ║")
    print("║   ██║  ███╗███████║██████╔╝  ███╔╝                             ║")
    print("║   ██║   ██║██╔══██║██╔══██╗ ███╔╝                              ║")
    print("║   ╚██████╔╝██║  ██║██║  ██║███████╗                            ║")
    print("║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                            ║")
    print("║                                                                ║")
    print("║   🔥 GARZ CYBER TOOLS v3.0 - TERMUX EDITION 🔥                ║")
    print("║                                                                ║")
    print("║   [*] Password Cracker    [*] Hash Generator                  ║")
    print("║   [*] Encoder/Decoder      [*] Network Scanner                ║")
    print("║   [*] OSINT Tools          [*] Crypto Tools                   ║")
    print("║                                                                ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("\033[0m")

def main_menu():
    while True:
        clear_screen()
        banner()
        print("\n\033[93m📌 MAIN MENU:\033[0m")
        print("════════════════════════════════════════════════════════════════")
        print("")
        print("  \033[92m[1]\033[0m  🔐 HASH GENERATOR & CRACKER")
        print("  \033[92m[2]\033[0m  📝 ENCODE / DECODE")
        print("  \033[92m[3]\033[0m  🔒 PASSWORD STRENGTH CHECKER")
        print("  \033[92m[4]\033[0m  🗝️  CRYPTOGRAPHY TOOLS (Caesar, XOR)")
        print("  \033[92m[5]\033[0m  🌐 NETWORK TOOLS")
        print("  \033[92m[6]\033[0m  🕵️  OSINT TOOLS")
        print("  \033[92m[7]\033[0m  💣 PASSWORD CRACKER")
        print("  \033[92m[8]\033[0m  🛠️  UTILITIES")
        print("  \033[92m[9]\033[0m  🚪 EXIT")
        print("")
        print("════════════════════════════════════════════════════════════════")
        
        choice = input("\n\033[96m⚡ Pilih menu (1-9): \033[0m")
        
        if choice == '1':
            hash_menu()
        elif choice == '2':
            encode_menu()
        elif choice == '3':
            from modules.password_checker import PasswordTools
            PasswordTools.password_checker()
            input("\n\033[93mTekan Enter...\033[0m")
        elif choice == '4':
            crypto_menu()
        elif choice == '5':
            network_menu()
        elif choice == '6':
            osint_menu()
        elif choice == '7':
            from modules.password_checker import PasswordTools
            PasswordTools.password_cracker()
            input("\n\033[93mTekan Enter...\033[0m")
        elif choice == '8':
            utilities_menu()
        elif choice == '9':
            print("\n\033[92m👋 Terima kasih telah menggunakan Garz Cyber Tools!\033[0m")
            sys.exit()
        else:
            print("\n\033[91m❌ Pilihan tidak valid!\033[0m")
            time.sleep(1)

def hash_menu():
    from modules.hasher import HashTools
    clear_screen()
    print("\n\033[93m🔐 HASH GENERATOR & CRACKER\033[0m\n")
    print("[1] Generate Hash (MD5, SHA1, SHA256)")
    print("[2] Hash File")
    print("[3] Kembali")
    
    choice = input("\n\033[96mPilih: \033[0m")
    if choice == '1':
        text = input("Masukkan teks: ")
        HashTools.generate_hash(text)
    elif choice == '2':
        filepath = input("Path file: ")
        HashTools.hash_file(filepath)
    input("\n\033[93mTekan Enter...\033[0m")

def encode_menu():
    from modules.encoder import EncoderTools
    clear_screen()
    print("\n\033[93m📝 ENCODE / DECODE TOOLS\033[0m\n")
    print("[1] Base64 Encode/Decode")
    print("[2] Hex Encode/Decode")
    print("[3] ROT13")
    print("[4] Kembali")
    
    choice = input("\n\033[96mPilih: \033[0m")
    if choice == '4':
        return
    
    text = input("Masukkan teks: ")
    
    if choice == '1':
        EncoderTools.base64_convert(text)
    elif choice == '2':
        EncoderTools.hex_convert(text)
    elif choice == '3':
        EncoderTools.rot13_convert(text)
    
    input("\n\033[93mTekan Enter...\033[0m")

def crypto_menu():
    from modules.crypto_tools import CryptoTools
    clear_screen()
    print("\n\033[93m🗝️ CRYPTOGRAPHY TOOLS\033[0m\n")
    print("[1] Caesar Cipher")
    print("[2] XOR Cipher")
    print("[3] Kembali")
    
    choice = input("\n\033[96mPilih: \033[0m")
    if choice == '3':
        return
    
    if choice == '1':
        text = input("Teks: ")
        shift = int(input("Shift (1-25): "))
        CryptoTools.caesar_cipher(text, shift)
    elif choice == '2':
        text = input("Teks: ")
        key = input("Key: ")
        CryptoTools.xor_cipher(text, key)
    
    input("\n\033[93mTekan Enter...\033[0m")

def network_menu():
    from modules.network_tools import NetworkTools
    clear_screen()
    print("\n\033[93m🌐 NETWORK TOOLS\033[0m\n")
    print("[1] Port Scanner")
    print("[2] IP Info")
    print("[3] Kembali")
    
    choice = input("\n\033[96mPilih: \033[0m")
    if choice == '3':
        return
    
    if choice == '1':
        target = input("Target IP/Domain: ")
        NetworkTools.port_scanner(target)
    elif choice == '2':
        target = input("IP/Domain: ")
        NetworkTools.get_ip_info(target)
    
    input("\n\033[93mTekan Enter...\033[0m")

def osint_menu():
    from modules.osint_tools import OsintTools
    clear_screen()
    print("\n\033[93m🕵️ OSINT TOOLS\033[0m\n")
    print("[1] DNS Lookup")
    print("[2] Kembali")
    
    choice = input("\n\033[96mPilih: \033[0m")
    if choice == '2':
        return
    
    domain = input("Domain target: ")
    
    if choice == '1':
        OsintTools.dns_lookup(domain)

def utilities_menu():
    from modules.password_checker import PasswordTools
    clear_screen()
    print("\n\033[93m🛠️ UTILITIES\033[0m\n")
    print("[1] Text Analyzer")
    print("[2] Random Password Generator")
    print("[3] Kembali")
    
    choice = input("\n\033[96mPilih: \033[0m")
    if choice == '1':
        text = input("Masukkan teks: ")
        PasswordTools.text_analyzer(text)
    elif choice == '2':
        length = int(input("Panjang password: "))
        PasswordTools.generate_password(length)
    else:
        return
    
    input("\n\033[93mTekan Enter...\033[0m")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n\033[92m👋 Terima kasih!\033[0m")
        sys.exit()
EOF
