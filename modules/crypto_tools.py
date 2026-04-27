cat > modules/crypto_tools.py << 'EOF'
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
        
        print(f"\n\033[92m✅ Hasil: {result}\033[0m")
    
    @staticmethod
    def xor_cipher(text, key):
        result = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
        print(f"\n\033[92m✅ Hasil XOR: {result}\033[0m")
        print("\n\033[93m💡 Jalankan lagi dengan output yang sama untuk dekripsi\033[0m")
EOF
