cat > garz_tools.py << 'EOF'
#!/usr/bin/env python3
import os
import sys
import time

def clear_screen():
    os.system('clear')

def banner():
    print("\033[91m")
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║   🔥 GARZ CYBER TOOLS v3.0 - TERMUX EDITION 🔥                ║")
    print("║   [*] Password Cracker    [*] Hash Generator                  ║")
    print("║   [*] Encoder/Decoder      [*] Network Scanner                ║")
    print("║   [*] OSINT Tools          [*] Crypto Tools                   ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    print("\033[0m")

def main_menu():
    while True:
        clear_screen()
        banner()
        print("\n\033[93m📌 MAIN MENU:\033[0m")
        print("════════════════════════════════════════════════════════════════")
        print("  \033[92m[1]\033[0m  🔐 HASH GENERATOR")
        print("  \033[92m[2]\033[0m  📝 ENCODE / DECODE")
        print("  \033[92m[3]\033[0m  🔒 PASSWORD CHECKER")
        print("  \033[92m[4]\033[0m  🗝️  CRYPTOGRAPHY TOOLS")
        print("  \033[92m[5]\033[0m  🌐 NETWORK TOOLS")
        print("  \033[92m[6]\033[0m  🕵️  OSINT TOOLS")
        print("  \033[92m[7]\033[0m  💣 PASSWORD CRACKER")
        print("  \033[92m[8]\033[0m  🛠️  UTILITIES")
        print("  \033[92m[9]\033[0m  🚪 EXIT")
        print("════════════════════════════════════════════════════════════════")
        
        choice = input("\n\033[96m⚡ Pilih menu (1-9): \033[0m")
        
        if choice == '1':
            from modules.hasher import HashTools
            clear_screen()
            text = input("Masukkan teks: ")
            HashTools.generate_hash(text)
            input("\nTekan Enter...")
        elif choice == '2':
            from modules.encoder import EncoderTools
            clear_screen()
            text = input("Masukkan teks: ")
            print("\n[1] Base64 Encode\n[2] Base64 Decode\n[3] Hex Encode\n[4] Hex Decode")
            opt = input("Pilih: ")
            if opt == '1':
                EncoderTools.base64_encode(text)
            elif opt == '2':
                EncoderTools.base64_decode(text)
            elif opt == '3':
                EncoderTools.hex_encode(text)
            elif opt == '4':
                EncoderTools.hex_decode(text)
            input("\nTekan Enter...")
        elif choice == '3':
            from modules.password_checker import PasswordTools
            clear_screen()
            pwd = input("Masukkan password: ")
            PasswordTools.check_password(pwd)
            input("\nTekan Enter...")
        elif choice == '4':
            from modules.crypto_tools import CryptoTools
            clear_screen()
            text = input("Teks: ")
            shift = int(input("Shift (1-25): "))
            CryptoTools.caesar_cipher(text, shift)
            input("\nTekan Enter...")
        elif choice == '5':
            from modules.network_tools import NetworkTools
            clear_screen()
            target = input("Target IP/Domain: ")
            NetworkTools.port_scanner(target)
            input("\nTekan Enter...")
        elif choice == '6':
            from modules.osint_tools import OsintTools
            clear_screen()
            domain = input("Domain: ")
            OsintTools.dns_lookup(domain)
            input("\nTekan Enter...")
        elif choice == '7':
            from modules.password_checker import PasswordTools
            clear_screen()
            target = input("Target password (demo): ")
            PasswordTools.brute_force(target)
            input("\nTekan Enter...")
        elif choice == '8':
            from modules.password_checker import PasswordTools
            clear_screen()
            length = int(input("Panjang password: "))
            PasswordTools.generate_password(length)
            input("\nTekan Enter...")
        elif choice == '9':
            print("\n\033[92m👋 Terima kasih!\033[0m")
            sys.exit()
        else:
            print("\n\033[91m❌ Pilihan salah!\033[0m")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n\033[92m👋 Terima kasih!\033[0m")
        sys.exit()
EOF
