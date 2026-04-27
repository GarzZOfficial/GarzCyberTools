cat > modules/encoder.py << 'EOF'
import base64

class EncoderTools:
    @staticmethod
    def base64_convert(text):
        print("\n[1] Encode")
        print("[2] Decode")
        choice = input("Pilih: ")
        if choice == '1':
            result = base64.b64encode(text.encode()).decode()
            print(f"\n\033[92m✅ Encode Base64: {result}\033[0m")
        elif choice == '2':
            try:
                result = base64.b64decode(text).decode()
                print(f"\n\033[92m✅ Decode Base64: {result}\033[0m")
            except:
                print("\n\033[91m❌ Invalid Base64!\033[0m")
    
    @staticmethod
    def hex_convert(text):
        print("\n[1] Encode to Hex")
        print("[2] Decode from Hex")
        choice = input("Pilih: ")
        if choice == '1':
            result = text.encode().hex()
            print(f"\n\033[92m✅ Hex: {result}\033[0m")
        elif choice == '2':
            try:
                result = bytes.fromhex(text).decode()
                print(f"\n\033[92m✅ Decoded: {result}\033[0m")
            except:
                print("\n\033[91m❌ Invalid Hex!\033[0m")
    
    @staticmethod
    def rot13_convert(text):
        result = text.translate(str.maketrans(
            'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
            'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm'
        ))
        print(f"\n\033[92m✅ ROT13: {result}\033[0m")
EOF
