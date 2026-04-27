cat > modules/crypto_tools.py << 'EOF'
class CryptoTools:
    @staticmethod
    def caesar_cipher(text, shift):
        print("\n[1] Enkripsi\n[2] Dekripsi")
        choice = input("Pilih: ")
        result = ""
        for char in text:
            if char.isalpha():
                offset = 65 if char.isupper() else 97
                if choice == '1':
                    result += chr((ord(char) - offset + shift) % 26 + offset)
                else:
                    result += chr((ord(char) - offset - shift) % 26 + offset)
            else:
                result += char
        print(f"\n\033[92m✅ Hasil: {result}\033[0m")
EOF
