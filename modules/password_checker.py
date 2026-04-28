cat > modules/password_checker.py << 'EOF'
import random
import string
import time
import re
import hashlib
from datetime import datetime

class PasswordTools:
    @staticmethod
    def check_password(pwd):
        """Check password strength with detailed analysis"""
        if not pwd:
            print("\n\033[91m❌ Password cannot be empty!\033[0m")
            return 0
        
        length = len(pwd)
        has_upper = any(c.isupper() for c in pwd)
        has_lower = any(c.islower() for c in pwd)
        has_digit = any(c.isdigit() for c in pwd)
        has_special = any(not c.isalnum() for c in pwd)
        
        # Common weak passwords
        common_passwords = ['password', '123456', 'qwerty', 'admin', 'letmein', 'welcome', 'monkey', 'abc123']
        is_common = pwd.lower() in common_passwords
        
        # Calculate score
        score = 0
        feedback = []
        
        # Length check
        if length >= 12:
            score += 2
            feedback.append("✅ Good length (12+ characters)")
        elif length >= 8:
            score += 1
            feedback.append("⚠️  Acceptable length (8-11 characters)")
        else:
            feedback.append("❌ Too short (minimum 8 characters)")
        
        # Character variety
        if has_upper and has_lower:
            score += 1
            feedback.append("✅ Mixed case letters")
        else:
            feedback.append("❌ Use both uppercase and lowercase")
        
        if has_digit:
            score += 1
            feedback.append("✅ Contains numbers")
        else:
            feedback.append("❌ Add numbers")
        
        if has_special:
            score += 1
            feedback.append("✅ Contains special characters")
        else:
            feedback.append("❌ Add special characters (!@#$%^&*)")
        
        # Common password penalty
        if is_common:
            score -= 2
            feedback.append("⚠️  Common password detected (easy to guess)")
        
        # Ensure score is between 0-5
        score = max(0, min(5, score))
        
        # Display results
        print("\n" + "="*50)
        print("\033[94m🔐 PASSWORD STRENGTH ANALYSIS\033[0m")
        print("="*50)
        
        # Strength meter
        if score == 5:
            strength = "VERY STRONG 💪💪💪"
            color = "\033[92m"
        elif score >= 4:
            strength = "STRONG 💪"
            color = "\033[92m"
        elif score >= 3:
            strength = "MEDIUM ⚠️"
            color = "\033[93m"
        else:
            strength = "WEAK ❌"
            color = "\033[91m"
        
        print(f"{color}💪 Password Strength: {strength}\033[0m")
        print(f"📊 Score: {score}/5")
        
        if is_common:
            print(f"\033[91m⚠️  WARNING: This is a commonly used password!\033[0m")
        
        print("\n\033[94mDetailed Analysis:\033[0m")
        for fb in feedback:
            print(f"  {fb}")
        
        # Additional info
        print(f"\n\033[94mStatistics:\033[0m")
        print(f"  Length      : {length} characters")
        print(f"  Uppercase   : {sum(1 for c in pwd if c.isupper())}")
        print(f"  Lowercase   : {sum(1 for c in pwd if c.islower())}")
        print(f"  Digits      : {sum(1 for c in pwd if c.isdigit())}")
        print(f"  Special     : {sum(1 for c in pwd if not c.isalnum())}")
        
        # Estimate crack time (very rough estimate)
        entropy = PasswordTools._calculate_entropy(pwd)
        print(f"  Entropy     : {entropy:.1f} bits")
        
        return score
    
    @staticmethod
    def _calculate_entropy(password):
        """Calculate password entropy in bits"""
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(not c.isalnum() for c in password):
            charset_size += 32
        
        if charset_size == 0:
            return 0
        
        entropy = len(password) * (charset_size.bit_length() - 1)
        return entropy
    
    @staticmethod
    def brute_force(target, max_length=4):
        """Brute force attack simulation (for educational purposes)"""
        print("\n" + "="*50)
        print("\033[93m⚠️  BRUTE FORCE SIMULATION (EDUCATIONAL)\033[0m")
        print("="*50)
        print(f"🎯 Target: {target}")
        print(f"🔧 Max length: {max_length}")
        print("-"*50)
        
        # Limit to lowercase letters and digits for speed
        chars = string.ascii_lowercase + string.digits
        attempts = 0
        start = time.time()
        
        for length in range(1, max_length + 1):
            print(f"\n📊 Trying length {length}...")
            for guess in PasswordTools._generate_combinations(chars, length):
                attempts += 1
                if attempts % 1000 == 0:
                    print(f"🔍 Attempts: {attempts} - Current: {guess.ljust(10)}", end='\r')
                
                if guess == target:
                    elapsed = time.time() - start
                    print(f"\n\n\033[92m✅ PASSWORD FOUND!\033[0m")
                    print(f"🔐 Password: {guess}")
                    print(f"📊 Total attempts: {attempts:,}")
                    print(f"⏱️  Time elapsed: {elapsed:.2f} seconds")
                    print(f"⚡ Speed: {attempts/elapsed:.0f} attempts/sec")
                    return True
        
        elapsed = time.time() - start
        print(f"\n\n\033[91m❌ PASSWORD NOT FOUND!\033[0m")
        print(f"📊 Total attempts: {attempts:,}")
        print(f"⏱️  Time elapsed: {elapsed:.2f} seconds")
        return False
    
    @staticmethod
    def _generate_combinations(chars, length):
        """Generate all combinations (iterative version, more efficient)"""
        if length == 0:
            yield ""
        else:
            for c in chars:
                for rest in PasswordTools._generate_combinations(chars, length - 1):
                    yield c + rest
    
    @staticmethod
    def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
        """Generate a strong random password"""
        if length < 8:
            print("\n\033[91m❌ Password length should be at least 8 characters\033[0m")
            length = 8
        
        # Build character set
        chars = ""
        if use_upper:
            chars += string.ascii_uppercase
        if use_lower:
            chars += string.ascii_lowercase
        if use_digits:
            chars += string.digits
        if use_special:
            chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        if not chars:
            chars = string.ascii_letters + string.digits
        
        # Ensure at least one of each type if requested
        password = []
        if use_upper:
            password.append(random.choice(string.ascii_uppercase))
        if use_lower:
            password.append(random.choice(string.ascii_lowercase))
        if use_digits:
            password.append(random.choice(string.digits))
        if use_special:
            password.append(random.choice("!@#$%^&*"))
        
        # Fill the rest randomly
        remaining = length - len(password)
        password.extend(random.choice(chars) for _ in range(remaining))
        
        # Shuffle
        random.shuffle(password)
        password = ''.join(password)
        
        print("\n" + "="*50)
        print("\033[92m🔐 GENERATED PASSWORD\033[0m")
        print("="*50)
        print(f"📝 Password: \033[92m{password}\033[0m")
        print(f"📏 Length: {len(password)} characters")
        
        # Check strength of generated password
        print("\n🔍 Strength Check:")
        PasswordTools.check_password(password)
        
        return password
    
    @staticmethod
    def check_breached(password):
        """Check if password has been breached using Have I Been Pwned API"""
        import requests
        
        print("\n" + "="*50)
        print("\033[94m🔍 CHECKING BREACH DATABASE\033[0m")
        print("="*50)
        
        try:
            # Hash the password
            sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
            prefix = sha1_hash[:5]
            suffix = sha1_hash[5:]
            
            # Query API
            url = f"https://api.pwnedpasswords.com/range/{prefix}"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                hashes = response.text.splitlines()
                for hash_entry in hashes:
                    if hash_entry.split(':')[0] == suffix:
                        count = int(hash_entry.split(':')[1])
                        print(f"\n\033[91m⚠️  PASSWORD HAS BEEN BREACHED!\033[0m")
                        print(f"📊 Found {count:,} times in data breaches")
                        print(f"🚨 Recommendation: DO NOT use this password!")
                        return True
                
                print(f"\n\033[92m✅ Password not found in breach database\033[0m")
                print("🔒 This password appears to be safe")
                return False
            else:
                print(f"\n\033[91m❌ API Error: {response.status_code}\033[0m")
                return None
                
        except ImportError:
            print("\n\033[91m❌ requests library not installed. Run: pip install requests\033[0m")
            return None
        except Exception as e:
            print(f"\n\033[91m❌ Error checking breach: {e}\033[0m")
            return None
    
    @staticmethod
    def password_policy_checker(password, policy=None):
        """Check password against custom policy"""
        if policy is None:
            policy = {
                'min_length': 8,
                'require_upper': True,
                'require_lower': True,
                'require_digit': True,
                'require_special': True,
                'max_consecutive': 3,
                'disallow_common': True
            }
        
        print("\n" + "="*50)
        print("\033[94m📋 PASSWORD POLICY CHECK\033[0m")
        print("="*50)
        
        violations = []
        
        # Check length
        if len(password) < policy['min_length']:
            violations.append(f"Minimum length {policy['min_length']} characters")
        
        # Check character requirements
        if policy.get('require_upper') and not any(c.isupper() for c in password):
            violations.append("At least one uppercase letter")
        
        if policy.get('require_lower') and not any(c.islower() for c in password):
            violations.append("At least one lowercase letter")
        
        if policy.get('require_digit') and not any(c.isdigit() for c in password):
            violations.append("At least one digit")
        
        if policy.get('require_special') and not any(not c.isalnum() for c in password):
            violations.append("At least one special character")
        
        # Check consecutive characters
        if policy.get('max_consecutive'):
            max_consecutive = 1
            current_count = 1
            for i in range(1, len(password)):
                if password[i] == password[i-1]:
                    current_count += 1
                    max_consecutive = max(max_consecutive, current_count)
                else:
                    current_count = 1
            
            if max_consecutive > policy['max_consecutive']:
                violations.append(f"No more than {policy['max_consecutive']} consecutive identical characters")
        
        # Check common passwords
        if policy.get('disallow_common'):
            common = ['password', '123456', 'qwerty', 'admin', 'letmein', 'welcome']
            if password.lower() in common:
                violations.append("Cannot use common passwords")
        
        # Display results
        if violations:
            print("\033[91m❌ Password does NOT meet policy requirements:\033[0m")
            for violation in violations:
                print(f"  • {violation}")
            return False
        else:
            print("\033[92m✅ Password meets all policy requirements!\033[0m")
            return True
    
    @staticmethod
    def generate_memorable_password():
        """Generate a memorable password using words"""
        common_words = [
            'tiger', 'eagle', 'dragon', 'phoenix', 'storm', 'thunder',
            'mountain', 'river', 'forest', 'ocean', 'sky', 'star',
            'brave', 'strong', 'wild', 'free', 'golden', 'silver',
            'summer', 'winter', 'spring', 'autumn', 'morning', 'night'
        ]
        
        # Pick random words
        word1 = random.choice(common_words)
        word2 = random.choice(common_words)
        number = random.randint(10, 99)
        special = random.choice(['!', '@', '#', '$', '&'])
        
        # Capitalize first letter
        word1 = word1.capitalize()
        word2 = word2.capitalize()
        
        # Different patterns
        patterns = [
            f"{word1}{word2}{number}{special}",
            f"{word1}{special}{word2}{number}",
            f"{word1}{number}{special}{word2}",
            f"{word1}_{word2}{number}{special}"
        ]
        
        password = random.choice(patterns)
        
        print("\n" + "="*50)
        print("\033[92m🔐 MEMORABLE PASSWORD GENERATOR\033[0m")
        print("="*50)
        print(f"📝 Password: \033[92m{password}\033[0m")
        print(f"💡 This password is easier to remember!")
        
        return password
    
    @staticmethod
    def batch_check_passwords(password_list):
        """Check multiple passwords at once"""
        print("\n" + "="*50)
        print("\033[94m📊 BATCH PASSWORD CHECK\033[0m")
        print("="*50)
        
        results = []
        for pwd in password_list:
            score = PasswordTools.check_password(pwd)
            results.append({
                'password': pwd,
                'score': score,
                'strength': 'Weak' if score <= 2 else 'Medium' if score <= 4 else 'Strong'
            })
            print("-"*50)
        
        # Summary
        print("\n\033[94m📈 SUMMARY:\033[0m")
        strong = sum(1 for r in results if r['strength'] == 'Strong')
        medium = sum(1 for r in results if r['strength'] == 'Medium')
        weak = sum(1 for r in results if r['strength'] == 'Weak')
        
        print(f"  Strong: {strong}")
        print(f"  Medium: {medium}")
        print(f"  Weak  : {weak}")
        
        return results

# Alias for backward compatibility
generate_password = PasswordTools.generate_password
check_password = PasswordTools.check_password
EOF
