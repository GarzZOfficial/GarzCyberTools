cat > modules/encoder.py << 'EOF'
import base64

class EncoderTools:
    @staticmethod
    def base64_encode(text):
        result = base64.b64encode(text.encode()).decode()
        print(f"\n\033[92m✅ Base64 Encode: {result}\033[0m")
    
    @staticmethod
    def base64_decode(text):
        try:
            result = base64.b64decode(text).decode()
            print(f"\n\033[92m✅ Base64 Decode: {result}\033[0m")
        except:
            print("\n\033[91m❌ Invalid Base64!\033[0m")
    
    @staticmethod
    def hex_encode(text):
        result = text.encode().hex()
        print(f"\n\033[92m✅ Hex Encode: {result}\033[0m")
    
    @staticmethod
    def hex_decode(text):
        try:
            result = bytes.fromhex(text).decode()
            print(f"\n\033[92m✅ Hex Decode: {result}\033[0m")
        except:
            print("\n\033[91m❌ Invalid Hex!\033[0m")
EOF
