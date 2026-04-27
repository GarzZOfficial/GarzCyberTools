cat > modules/password_checker.py << 'EOF'
import random
import string
import time

class PasswordTools:
    @staticmethod
    def password_checker():
        pwd = input("\n\033[96m🔐 Masukkan password: \033[0m")
        length = len(pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_lower = any(c.islower() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(not c.isalnum() for c in pwd)
        
        score = 0
        feedback = []
        
        if length >= 8:
            score += 1
        else:
            feedback.append("❌ Password terlalu pendek (minimal 8 karakter)")
        
        if length >= 12:
            score += 1
            feedback.append("✅ Panjang password bagus (12+ karakter)")
        
        if has_upper and has_lower:
            score += 1
            feedback.append("✅ Kombinasi huruf besar & kecil")
        else:
            feedback.append("❌ Tambahkan huruf besar dan kecil")
        
        if has_digit:
            score += 1
            feedback.append("✅ Mengandung angka")
        else:
            feedback.append("❌ Tambahkan angka")
        
        if has_special:
            score += 1
            feedback.append("✅ Mengandung karakter khusus")
        else:
            feedback.append("❌ Tambahkan karakter khusus (!@#$%^&*)")
        
        print("\n" + "="*50)
        print("\033[93m🔍 ANALISIS PASSWORD:\033[0m")
        print("="*50)
        for f in feedback:
            print(f)
        
        if score <= 2:
            strength = "LEMAH ❌"
            color = "\033[91m"
        elif score <= 4:
            strength = "SEDANG ⚠️"
            color = "\033[93m"
        else:
            strength = "KUAT ✅"
            color = "\033[92m"
        
        print(f"\n{color}💪 Kekuatan Password: {strength}\033[0m")
        print(f"📊 Skor: {score}/6")
    
    @staticmethod
    def password_cracker():
        print("\n\033[93m💣 PASSWORD CRACKER (Brute Force Demo)\033[0m")
        print("="*40)
        target = input("\033[96mTarget password (demo): \033[0m")
        
        chars = string.ascii_lowercase + string.digits
        max_length = 4
        
        start_time = time.time()
        attempts = 0
        
        for length in range(1, max_length + 1):
            for guess in PasswordTools._generate_combinations(chars, length):
                attempts += 1
                if attempts % 1000 == 0:
                    print(f"🔍 Mencoba: {guess}...", end='\r')
                
                if guess == target:
                    elapsed = time.time() - start_time
                    print(f"\n\n\033[92m✅ PASSWORD DITEMUKAN!\033[0m")
                    print(f"Password: {guess}")
                    print(f"Attempts: {attempts}")
                    print(f"Waktu: {elapsed:.2f} detik")
                    return
        
        print("\n\033[91m❌ Password tidak ditemukan!\033[0m")
    
    @staticmethod
    def _generate_combinations(chars, length):
        if length == 0:
            yield ""
        else:
            for c in chars:
                for rest in PasswordTools._generate_combinations(chars, length - 1):
                    yield c + rest
    
    @staticmethod
    def text_analyzer(text):
        print("\n\033[93m📊 TEXT ANALYZER\033[0m")
        print("="*40)
        print(f"📝 Teks: {text[:100]}{'...' if len(text) > 100 else ''}")
        print(f"📏 Panjang: {len(text)} karakter")
        print(f"🔤 Jumlah kata: {len(text.split())}")
        print(f"🔢 Angka: {sum(c.isdigit() for c in text)}")
        print(f"🔡 Huruf: {sum(c.isalpha() for c in text)}")
        print(f"✨ Huruf besar: {sum(c.isupper() for c in text)}")
        print(f"🔽 Huruf kecil: {sum(c.islower() for c in text)}")
    
    @staticmethod
    def generate_password(length=12):
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"\n\033[92m✅ Password generated: {password}\033[0m")
EOF
