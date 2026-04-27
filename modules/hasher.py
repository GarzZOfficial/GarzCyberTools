cat > modules/hasher.py << 'EOF'
import hashlib

class HashTools:
    @staticmethod
    def generate_hash(text):
        print(f"\n\033[92m📝 Teks: {text}\033[0m")
        print(f"\n\033[93mMD5\033[0m     : {hashlib.md5(text.encode()).hexdigest()}")
        print(f"\033[93mSHA1\033[0m    : {hashlib.sha1(text.encode()).hexdigest()}")
        print(f"\033[93mSHA256\033[0m  : {hashlib.sha256(text.encode()).hexdigest()}")
EOF
