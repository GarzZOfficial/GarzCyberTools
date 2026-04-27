cat > modules/hasher.py << 'EOF'
import hashlib

class HashTools:
    @staticmethod
    def generate_hash(text):
        print(f"\n\033[92m📝 Teks: {text}\033[0m")
        print(f"\n\033[93mMD5\033[0m     : {hashlib.md5(text.encode()).hexdigest()}")
        print(f"\033[93mSHA1\033[0m    : {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"\033[93mSHA256\033[0m  : {hashlib.sha256(text.encode()).hexdigest()}")
    
    @staticmethod
    def hash_file(filepath):
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
                print(f"\n\033[92m📁 File: {filepath}\033[0m")
                print(f"\n\033[93mMD5\033[0m    : {hashlib.md5(data).hexdigest()}")
                print(f"\033[93mSHA256\033[0m : {hashlib.sha256(data).hexdigest()}")
        except FileNotFoundError:
            print("\n\033[91m❌ File tidak ditemukan!\033[0m")
EOF
