import base64
import urllib.parse

class EncoderTools:
    @staticmethod
    def base64_convert(text):
        print("\n[1] Encode")
        print("[2] Decode")
        choice = input("Pilih: ")
        if choice == '1':
            result = base64.b64encode(text.encode()).decode()
            print(f"\n✅ Encode Base64: {result}")
        elif choice == '2':
            try:
                result = base64.b64decode(text).decode()
                print(f"\n✅ Decode Base64: {result}")
            except:
                print("❌ Invalid Base64!")
        else:
            print("❌ Pilihan salah!")
    
    @staticmethod
    def hex_convert(text):
        print("\n[1] Encode to Hex")
        print("[2] Decode from Hex")
        choice = input("Pilih: ")
        if choice == '1':
            result = text.encode().hex()
            print(f"\n✅ Hex: {result}")
        elif choice == '2':
            try:
                result = bytes.fromhex(text).decode()
                print(f"\n✅ Decoded: {result}")
            except:
                print("❌ Invalid Hex!")
        else:
            print("❌ Pilihan salah!")
    
    @staticmethod
    def rot13_convert(text):
        result = text.translate(str.maketrans(
            'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
            'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm'
        ))
        print(f"\n✅ ROT13: {result}")
    
    @staticmethod
    def url_convert(text):
        print("\n[1] URL Encode")
        print("[2] URL Decode")
        choice = input("Pilih: ")
        if choice == '1':
            result = urllib.parse.quote(text)
            print(f"\n✅ URL Encode: {result}")
        elif choice == '2':
            result = urllib.parse.unquote(text)
            print(f"\n✅ URL Decode: {result}")
        else:
            print("❌ Pilihan salah!")
    
    @staticmethod
    def binary_convert(text):
        print("\n[1] Text to Binary")
        print("[2] Binary to Text")
        choice = input("Pilih: ")
        if choice == '1':
            result = ' '.join(format(ord(c), '08b') for c in text)
            print(f"\n✅ Binary: {result}")
        elif choice == '2':
            try:
                binary_values = text.split()
                result = ''.join(chr(int(bv, 2)) for bv in binary_values)
                print(f"\n✅ Text: {result}")
            except:
                print("❌ Invalid Binary!")
        else:
            print("❌ Pilihan salah!")
