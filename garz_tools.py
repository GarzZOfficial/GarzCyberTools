cat > garz_tools.py << 'EOF'
#!/usr/bin/env python3
"""
GARZ CYBER TOOLS v3.0 - Ultimate Cybersecurity Toolkit
Author: Garz Cyber Security Team
Version: 3.0
"""

import os
import sys
import time
import subprocess
from datetime import datetime

# Try to import colorama for better Windows support
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RESET = Style.RESET_ALL
except ImportError:
    # Fallback ANSI codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')

def check_dependencies():
    """Check if required modules are installed"""
    required_modules = ['modules.hasher', 'modules.encoder', 'modules.password_checker', 
                       'modules.crypto_tools', 'modules.network_tools', 'modules.osint_tools']
    
    missing = []
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            missing.append(module)
    
    if missing:
        print(f"{RED}❌ Missing modules: {', '.join(missing)}{RESET}")
        print(f"{YELLOW}📌 Run: pip install -r requirements.txt{RESET}")
        return False
    return True

def loading_animation(text="Loading", duration=1):
    """Show loading animation"""
    animation = "⣾⣽⣻⢿⡿⣟⣯⣷"
    for i in range(int(duration * 10)):
        sys.stdout.write(f"\r{text} {animation[i % len(animation)]}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\r" + " " * 30 + "\r")

def banner():
    """Display main banner"""
    clear_screen()
    print(f"{RED}")
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                              ║")
    print("║   ██████╗  █████╗ ██████╗ ███████╗                                         ║")
    print("║   ██╔════╝ ██╔══██╗██╔══██╗╚══███╔╝                                         ║")
    print("║   ██║  ███╗███████║██████╔╝  ███╔╝                                          ║")
    print("║   ██║   ██║██╔══██║██╔══██╗ ███╔╝                                           ║")
    print("║   ╚██████╔╝██║  ██║██║  ██║███████╗                                         ║")
    print("║    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝                                         ║")
    print("║                                                                              ║")
    print(f"║   {WHITE}🔥 GARZ CYBER TOOLS v3.0 - TERMUX EDITION 🔥{RED}                              ║")
    print("║                                                                              ║")
    print("║   ╔══════════════════════════════════════════════════════════════════════╗   ║")
    print(f"║   ║  {GREEN}[*] Password Cracker{RED}      {GREEN}[*] Hash Generator{RED}      {GREEN}[*] Encoder/Decoder{RED} ║   ║")
    print(f"║   ║  {GREEN}[*] Network Scanner{RED}       {GREEN}[*] OSINT Tools{RED}         {GREEN}[*] Crypto Tools{RED}    ║   ║")
    print(f"║   ║  {GREEN}[*] Port Scanner{RED}          {GREEN}[*] DNS Lookup{RED}          {GREEN}[*] WHOIS Lookup{RED}    ║   ║")
    print("║   ╚══════════════════════════════════════════════════════════════════════╝   ║")
    print("║                                                                              ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")
    print(f"{RESET}")

def hash_generator_menu():
    """Hash generator menu"""
    from modules.hasher import HashTools
    
    clear_screen()
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         🔐 HASH GENERATOR TOOLS           ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}")
    print()
    
    print(f"{CYAN}[1] Generate All Hashes{RESET}")
    print(f"{CYAN}[2] Simple Hash (Single Algorithm){RESET}")
    print(f"{CYAN}[3] Hash File{RESET}")
    print(f"{CYAN}[4] Verify Hash{RESET}")
    print(f"{CYAN}[5] Back to Main Menu{RESET}")
    print()
    
    choice = input(f"{YELLOW}⚡ Pilih menu (1-5): {RESET}")
    
    if choice == '1':
        text = input("Masukkan teks: ")
        if text:
            HashTools.generate_hash(text)
        else:
            print(f"{RED}❌ Teks tidak boleh kosong!{RESET}")
    
    elif choice == '2':
        text = input("Masukkan teks: ")
        algo = input("Algoritma (md5/sha1/sha256/sha512) [sha256]: ") or "sha256"
        if text:
            HashTools.simple_hash(text, algo)
        else:
            print(f"{RED}❌ Teks tidak boleh kosong!{RESET}")
    
    elif choice == '3':
        filepath = input("Masukkan path file: ")
        if os.path.exists(filepath):
            HashTools.hash_file(filepath)
        else:
            print(f"{RED}❌ File tidak ditemukan!{RESET}")
    
    elif choice == '4':
        text = input("Masukkan teks: ")
        hash_value = input("Masukkan hash: ")
        algo = input("Algoritma [sha256]: ") or "sha256"
        if text and hash_value:
            HashTools.verify_hash(text, hash_value, algo)
        else:
            print(f"{RED}❌ Data tidak lengkap!{RESET}")
    
    input(f"\n{BLUE}📌 Tekan Enter untuk kembali...{RESET}")

def encode_decode_menu():
    """Encode/Decode menu"""
    from modules.encoder import EncoderTools
    
    clear_screen()
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         📝 ENCODE / DECODE TOOLS          ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}")
    print()
    
    print(f"{CYAN}[1] Base64 Encode{RESET}")
    print(f"{CYAN}[2] Base64 Decode{RESET}")
    print(f"{CYAN}[3] Hex Encode{RESET}")
    print(f"{CYAN}[4] Hex Decode{RESET}")
    print(f"{CYAN}[5] ROT13 Encode/Decode{RESET}")
    print(f"{CYAN}[6] URL Encode{RESET}")
    print(f"{CYAN}[7] URL Decode{RESET}")
    print(f"{CYAN}[8] Binary Encode{RESET}")
    print(f"{CYAN}[9] Binary Decode{RESET}")
    print(f"{CYAN}[10] Back to Main Menu{RESET}")
    print()
    
    choice = input(f"{YELLOW}⚡ Pilih menu (1-10): {RESET}")
    text = input("Masukkan teks: ")
    
    if choice == '1':
        EncoderTools.base64_encode(text)
    elif choice == '2':
        EncoderTools.base64_decode(text)
    elif choice == '3':
        EncoderTools.hex_encode(text)
    elif choice == '4':
        EncoderTools.hex_decode(text)
    elif choice == '5':
        EncoderTools.rot13(text)
    elif choice == '6':
        EncoderTools.url_encode(text)
    elif choice == '7':
        EncoderTools.url_decode(text)
    elif choice == '8':
        binary = ' '.join(format(ord(c), '08b') for c in text)
        print(f"{GREEN}✅ Binary: {binary}{RESET}")
    elif choice == '9':
        try:
            text = text.replace(' ', '')
            decoded = ''.join(chr(int(text[i:i+8], 2)) for i in range(0, len(text), 8))
            print(f"{GREEN}✅ Decoded: {decoded}{RESET}")
        except:
            print(f"{RED}❌ Invalid binary!{RESET}")
    
    input(f"\n{BLUE}📌 Tekan Enter untuk kembali...{RESET}")

def password_checker_menu():
    """Password checker menu"""
    from modules.password_checker import PasswordTools
    
    clear_screen()
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         🔒 PASSWORD CHECKER TOOLS         ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}")
    print()
    
    print(f"{CYAN}[1] Check Password Strength{RESET}")
    print(f"{CYAN}[2] Check Breached Password{RESET}")
    print(f"{CYAN}[3] Generate Strong Password{RESET}")
    print(f"{CYAN}[4] Generate Memorable Password{RESET}")
    print(f"{CYAN}[5] Back to Main Menu{RESET}")
    print()
    
    choice = input(f"{YELLOW}⚡ Pilih menu (1-5): {RESET}")
    
    if choice == '1':
        pwd = input("Masukkan password: ")
        if pwd:
            PasswordTools.check_password(pwd)
        else:
            print(f"{RED}❌ Password tidak boleh kosong!{RESET}")
    
    elif choice == '2':
        pwd = input("Masukkan password: ")
        if pwd:
            loading_animation("Checking breach database", 1)
            PasswordTools.check_breached(pwd)
        else:
            print(f"{RED}❌ Password tidak boleh kosong!{RESET}")
    
    elif choice == '3':
        length = input("Panjang password [16]: ") or "16"
        try:
            PasswordTools.generate_password(int(length))
        except ValueError:
            PasswordTools.generate_password(16)
    
    elif choice == '4':
        PasswordTools.generate_memorable_password()
    
    input(f"\n{BLUE}📌 Tekan Enter untuk kembali...{RESET}")

def crypto_tools_menu():
    """Cryptography tools menu"""
    from modules.crypto_tools import CryptoTools
    
    clear_screen()
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         🗝️  CRYPTOGRAPHY TOOLS            ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}")
    print()
    
    print(f"{CYAN}[1] Caesar Cipher{RESET}")
    print(f"{CYAN}[2] Caesar Brute Force{RESET}")
    print(f"{CYAN}[3] Back to Main Menu{RESET}")
    print()
    
    choice = input(f"{YELLOW}⚡ Pilih menu (1-3): {RESET}")
    
    if choice == '1':
        text = input("Masukkan teks: ")
        try:
            shift = int(input("Shift (1-25): "))
            if 1 <= shift <= 25:
                CryptoTools.caesar_cipher(text, shift)
            else:
                print(f"{RED}❌ Shift harus antara 1-25!{RESET}")
        except ValueError:
            print(f"{RED}❌ Shift harus angka!{RESET}")
    
    elif choice == '2':
        text = input("Masukkan ciphertext: ")
        CryptoTools.caesar_brute_force(text)
    
    input(f"\n{BLUE}📌 Tekan Enter untuk kembali...{RESET}")

def network_tools_menu():
    """Network tools menu"""
    from modules.network_tools import NetworkTools
    
    clear_screen()
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         🌐 NETWORK TOOLS                  ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}")
    print()
    
    print(f"{CYAN}[1] DNS Lookup (Domain to IP){RESET}")
    print(f"{CYAN}[2] Reverse DNS (IP to Domain){RESET}")
    print(f"{CYAN}[3] Port Scanner{RESET}")
    print(f"{CYAN}[4] Ping Host{RESET}")
    print(f"{CYAN}[5] Back to Main Menu{RESET}")
    print()
    
    choice = input(f"{YELLOW}⚡ Pilih menu (1-5): {RESET}")
    
    if choice == '1':
        target = input("Masukkan domain: ")
        if target:
            NetworkTools.get_ip(target)
        else:
            print(f"{RED}❌ Domain tidak boleh kosong!{RESET}")
    
    elif choice == '2':
        ip = input("Masukkan IP address: ")
        if ip:
            NetworkTools.reverse_dns(ip)
        else:
            print(f"{RED}❌ IP tidak boleh kosong!{RESET}")
    
    elif choice == '3':
        host = input("Masukkan host/IP: ")
        if host:
            print(f"{YELLOW}Scanning common ports...{RESET}")
            ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 993, 995, 3306, 3389, 5432, 5900, 8080, 8443]
            NetworkTools.port_scan(host, ports)
        else:
            print(f"{RED}❌ Host tidak boleh kosong!{RESET}")
    
    elif choice == '4':
        host = input("Masukkan host/IP: ")
        if host:
            NetworkTools.ping_host(host)
        else:
            print(f"{RED}❌ Host tidak boleh kosong!{RESET}")
    
    input(f"\n{BLUE}📌 Tekan Enter untuk kembali...{RESET}")

def osint_tools_menu():
    """OSINT tools menu"""
    from modules.osint_tools import OsintTools
    
    clear_screen()
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         🕵️  OSINT TOOLS                   ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}")
    print()
    
    print(f"{CYAN}[1] IP Geolocation{RESET}")
    print(f"{CYAN}[2] DNS Records{RESET}")
    print(f"{CYAN}[3] WHOIS Lookup{RESET}")
    print(f"{CYAN}[4] Email Validation{RESET}")
    print(f"{CYAN}[5] Subdomain Scanner{RESET}")
    print(f"{CYAN}[6] Back to Main Menu{RESET}")
    print()
    
    choice = input(f"{YELLOW}⚡ Pilih menu (1-6): {RESET}")
    
    if choice == '1':
        ip = input("Masukkan IP address (kosongkan untuk IP sendiri): ")
        if ip.strip():
            OsintTools.get_geoip(ip)
        else:
            OsintTools.get_geoip()
    
    elif choice == '2':
        domain = input("Masukkan domain: ")
        record = input("Record type (A/MX/NS/TXT) [A]: ") or "A"
        if domain:
            OsintTools.dns_records(domain, record)
        else:
            print(f"{RED}❌ Domain tidak boleh kosong!{RESET}")
    
    elif choice == '3':
        domain = input("Masukkan domain: ")
        if domain:
            OsintTools.whois_lookup(domain)
        else:
            print(f"{RED}❌ Domain tidak boleh kosong!{RESET}")
    
    elif choice == '4':
        email = input("Masukkan email: ")
        if email:
            OsintTools.email_validation(email)
        else:
            print(f"{RED}❌ Email tidak boleh kosong!{RESET}")
    
    elif choice == '5':
        domain = input("Masukkan domain: ")
        if domain:
            loading_animation("Scanning subdomains", 1)
            OsintTools.subdomain_scan(domain)
        else:
            print(f"{RED}❌ Domain tidak boleh kosong!{RESET}")
    
    input(f"\n{BLUE}📌 Tekan Enter untuk kembali...{RESET}")

def password_cracker_menu():
    """Password cracker menu"""
    from modules.password_checker import PasswordTools
    
    clear_screen()
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         💣 PASSWORD CRACKER               ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}")
    print()
    print(f"{RED}⚠️  WARNING: Educational purposes only!{RESET}")
    print()
    
    print(f"{CYAN}[1] Brute Force Attack (Demo){RESET}")
    print(f"{CYAN}[2] Back to Main Menu{RESET}")
    print()
    
    choice = input(f"{YELLOW}⚡ Pilih menu (1-2): {RESET}")
    
    if choice == '1':
        target = input("Target password (max 4 chars for demo): ")
        if target:
            if len(target) <= 4:
                PasswordTools.brute_force(target, 4)
            else:
                print(f"{YELLOW}⚠️  Demo limited to 4 characters for speed{RESET}")
                PasswordTools.brute_force(target[:4], 4)
        else:
            print(f"{RED}❌ Target tidak boleh kosong!{RESET}")
    
    input(f"\n{BLUE}📌 Tekan Enter untuk kembali...{RESET}")

def utilities_menu():
    """Utilities menu"""
    from modules.password_checker import PasswordTools
    
    clear_screen()
    print(f"{GREEN}╔════════════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║         🛠️  UTILITIES                     ║{RESET}")
    print(f"{GREEN}╚════════════════════════════════════════════╝{RESET}")
    print()
    
    print(f"{CYAN}[1] Text Analyzer{RESET}")
    print(f"{CYAN}[2] Password Generator{RESET}")
    print(f"{CYAN}[3] System Info{RESET}")
    print(f"{CYAN}[4] Back to Main Menu{RESET}")
    print()
    
    choice = input(f"{YELLOW}⚡ Pilih menu (1-4): {RESET}")
    
    if choice == '1':
        text = input("Masukkan teks: ")
        if text:
            print(f"\n{GREEN}📊 Text Analysis:{RESET}")
            print(f"  Characters: {len(text)}")
            print(f"  Words: {len(text.split())}")
            print(f"  Lines: {len(text.splitlines())}")
            print(f"  Uppercase: {sum(1 for c in text if c.isupper())}")
            print(f"  Lowercase: {sum(1 for c in text if c.islower())}")
            print(f"  Digits: {sum(1 for c in text if c.isdigit())}")
            print(f"  Spaces: {sum(1 for c in text if c.isspace())}")
        else:
            print(f"{RED}❌ Teks tidak boleh kosong!{RESET}")
    
    elif choice == '2':
        length = input("Panjang password [16]: ") or "16"
        try:
            PasswordTools.generate_password(int(length))
        except ValueError:
            PasswordTools.generate_password(16)
    
    elif choice == '3':
        print(f"\n{GREEN}💻 System Information:{RESET}")
        print(f"  OS: {os.name}")
        print(f"  Python: {sys.version.split()[0]}")
        print(f"  Platform: {sys.platform}")
    
    input(f"\n{BLUE}📌 Tekan Enter untuk kembali...{RESET}")

def main_menu():
    """Main menu function"""
    while True:
        try:
            banner()
            print(f"\n{YELLOW}📌 MAIN MENU:{RESET}")
            print("═══════════════════════════════════════════════════════════════════════════════")
            print(f"  {GREEN}[1]{RESET}  🔐 HASH GENERATOR & CRACKER")
            print(f"  {GREEN}[2]{RESET}  📝 ENCODE / DECODE (Base64, Hex, ROT13, URL, Binary)")
            print(f"  {GREEN}[3]{RESET}  🔒 PASSWORD STRENGTH CHECKER")
            print(f"  {GREEN}[4]{RESET}  🗝️  CRYPTOGRAPHY TOOLS (Caesar Cipher)")
            print(f"  {GREEN}[5]{RESET}  🌐 NETWORK TOOLS (Port Scanner, DNS Lookup)")
            print(f"  {GREEN}[6]{RESET}  🕵️  OSINT TOOLS (IP Info, DNS Records, WHOIS)")
            print(f"  {GREEN}[7]{RESET}  💣 PASSWORD CRACKER (Brute Force Demo)")
            print(f"  {GREEN}[8]{RESET}  🛠️  UTILITIES (Text Analyzer, Password Generator)")
            print(f"  {GREEN}[9]{RESET}  🚪 EXIT")
            print("═══════════════════════════════════════════════════════════════════════════════")
            
            choice = input(f"\n{CYAN}⚡ Pilih menu (1-9): {RESET}")
            
            if choice == '1':
                hash_generator_menu()
            elif choice == '2':
                encode_decode_menu()
            elif choice == '3':
                password_checker_menu()
            elif choice == '4':
                crypto_tools_menu()
            elif choice == '5':
                network_tools_menu()
            elif choice == '6':
                osint_tools_menu()
            elif choice == '7':
                password_cracker_menu()
            elif choice == '8':
                utilities_menu()
            elif choice == '9':
                print(f"\n{GREEN}")
                print("╔════════════════════════════════════════════╗")
                print("║     👋 Terima kasih telah menggunakan!     ║")
                print("║        GARZ CYBER TOOLS v3.0               ║")
                print("╚════════════════════════════════════════════╝")
                print(f"{RESET}")
                sys.exit(0)
            else:
                print(f"\n{RED}❌ Pilihan tidak valid!{RESET}")
                time.sleep(1)
                
        except KeyboardInterrupt:
            print(f"\n\n{GREEN}👋 Terima kasih!{RESET}")
            sys.exit(0)
        except Exception as e:
            print(f"\n{RED}❌ Error: {e}{RESET}")
            print(f"{YELLOW}📌 Silakan laporkan bug ke developer{RESET}")
            time.sleep(2)

if __name__ == "__main__":
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    # Run main menu
    main_menu()
EOF
