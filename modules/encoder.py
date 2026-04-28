cat > modules/encoder.py << 'EOF'
import base64
import binascii

class EncoderTools:
    @staticmethod
    def base64_encode(text):
        """Encode text ke Base64"""
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        try:
            result = base64.b64encode(text.encode('utf-8')).decode('utf-8')
            print(f"\n\033[92m✅ Base64 Encode: {result}\033[0m")
            return result
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def base64_decode(text):
        """Decode Base64 ke text asli"""
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        try:
            # Tambahkan padding jika diperlukan
            missing_padding = len(text) % 4
            if missing_padding:
                text += '=' * (4 - missing_padding)
            
            result = base64.b64decode(text).decode('utf-8')
            print(f"\n\033[92m✅ Base64 Decode: {result}\033[0m")
            return result
        except binascii.Error:
            print("\n\033[91m❌ Invalid Base64 format!\033[0m")
            return None
        except UnicodeDecodeError:
            print("\n\033[91m❌ Decoded data is not valid UTF-8 text!\033[0m")
            return None
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def hex_encode(text):
        """Encode text ke Hexadecimal"""
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        try:
            result = text.encode('utf-8').hex()
            # Format output dengan spasi setiap 2 karakter (opsional)
            formatted = ' '.join(result[i:i+2] for i in range(0, len(result), 2))
            print(f"\n\033[92m✅ Hex Encode: {result}\033[0m")
            print(f"\033[90m   Formatted: {formatted}\033[0m")
            return result
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def hex_decode(text):
        """Decode Hexadecimal ke text asli"""
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        try:
            # Hapus spasi jika ada
            text = text.replace(' ', '').replace('\n', '')
            
            # Validasi panjang hex (harus genap)
            if len(text) % 2 != 0:
                print("\n\033[91m❌ Invalid Hex: length must be even!\033[0m")
                return None
            
            result = bytes.fromhex(text).decode('utf-8')
            print(f"\n\033[92m✅ Hex Decode: {result}\033[0m")
            return result
        except ValueError:
            print("\n\033[91m❌ Invalid Hex characters!\033[0m")
            return None
        except UnicodeDecodeError:
            print("\n\033[91m❌ Decoded data is not valid UTF-8 text!\033[0m")
            return None
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def rot13(text):
        """ROT13 cipher (paling sederhana)"""
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        
        result = []
        for char in text:
            if 'a' <= char <= 'z':
                result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
            elif 'A' <= char <= 'Z':
                result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
            else:
                result.append(char)
        
        result_text = ''.join(result)
        print(f"\n\033[92m✅ ROT13: {result_text}\033[0m")
        return result_text
    
    @staticmethod
    def url_encode(text):
        """URL Encode"""
        from urllib.parse import quote
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        try:
            result = quote(text, safe='')
            print(f"\n\033[92m✅ URL Encode: {result}\033[0m")
            return result
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def url_decode(text):
        """URL Decode"""
        from urllib.parse import unquote
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        try:
            result = unquote(text)
            print(f"\n\033[92m✅ URL Decode: {result}\033[0m")
            return result
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
EOF
