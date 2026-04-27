cat > modules/password_checker.py << 'EOF'
import random
import string
import time

class PasswordTools:
    @staticmethod
    def check_password(pwd):
        length = len(pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_lower = any(c.islower() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(not c.isalnum() for c in pwd)
        
        score = 0
        if length >= 8:
            score += 1
        if length >= 12:
            score += 1
        if has_upper and has_lower:
            score += 1
        if has_digit:
            score += 1
        if has_special:
            score += 1
        
        print("\n" + "="*40)
        if score <= 2:
            print("\033[91m💪 Kekuatan Password: LEMAH ❌\033[0m")
        elif score <= 4:
            print("\033[93m💪 Kekuatan Password: SEDANG ⚠️\033[0m")
        else:
            print("\033[92m💪 Kekuatan Password: KUAT ✅\033[0m")
        print(f"📊 Skor: {score}/5")
    
    @staticmethod
    def brute_force(target):
        chars = string.ascii_lowercase + string.digits
        max_length = 4
        attempts = 0
        start = time.time()
        
        for length in range(1, max_length + 1):
            for guess in PasswordTools._generate(chars, length):
                attempts += 1
                if attempts % 1000 == 0:
                    print(f"🔍 Mencoba: {guess}...", end='\r')
                if guess == target:
                    elapsed = time.time() - start
                    print(f"\n\n\033[92m✅ DITEMUKAN! Password: {guess}\033[0m")
                    print(f"📊 Percobaan: {attempts}, Waktu: {elapsed:.2f}s")
                    return
        print("\n\033[91m❌ Password tidak ditemukan!\033[0m")
    
    @staticmethod
    def _generate(chars, length):
        if length == 0:
            yield ""
        else:
            for c in chars:
                for rest in PasswordTools._generate(chars, length - 1):
                    yield c + rest
    
    @staticmethod
    def generate_password(length):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"\n\033[92m✅ Password: {password}\033[0m")
EOF
