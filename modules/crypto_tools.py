cat > modules/crypto_tools.py << 'EOF'
class CryptoTools:
    @staticmethod
    def caesar_cipher(text, shift=None):
        print("\n[1] Enkripsi\n[2] Dekripsi")
        choice = input("Pilih: ")
        
        if choice not in ['1', '2']:
            print("\033[91m❌ Pilihan tidak valid!\033[0m")
            return
        
        if shift is None:
            try:
                shift = int(input("Masukkan shift (1-25): "))
            except ValueError:
                print("\033[91m❌ Shift harus berupa angka!\033[0m")
                return
        
        result = ""
        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                if choice == '1':  # Enkripsi
                    result += chr((ord(char) - offset + shift) % 26 + offset)
                else:  # Dekripsi
                    result += chr((ord(char) - offset - shift) % 26 + offset)
            else:
                result += char
        
        print(f"\n\033[92m✅ Hasil: {result}\033[0m")
        return result
    
    @staticmethod
    def caesar_brute_force(ciphertext):
        """Mencoba semua kemungkinan shift (1-25)"""
        print("\n\033[93m🔓 Mencoba semua kemungkinan shift...\033[0m")
        for shift in range(1, 26):
            result = ""
            for char in ciphertext:
                if char.isalpha():
                    offset = 65 if char.isupper() else 97
                    result += chr((ord(char) - offset - shift) % 26 + offset)
                else:
                    result += char
            print(f"Shift {shift:2d}: {result}")
EOF
