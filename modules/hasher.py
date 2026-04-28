cat > modules/hasher.py << 'EOF'
import hashlib
import os

class HashTools:
    @staticmethod
    def generate_hash(text):
        """Generate berbagai hash dari text"""
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        
        text_bytes = text.encode('utf-8')
        
        print(f"\n\033[92m📝 Teks: {text}\033[0m")
        print("="*60)
        
        hashes = {
            'MD5': hashlib.md5(text_bytes).hexdigest(),
            'SHA1': hashlib.sha1(text_bytes).hexdigest(),
            'SHA224': hashlib.sha224(text_bytes).hexdigest(),
            'SHA256': hashlib.sha256(text_bytes).hexdigest(),
            'SHA384': hashlib.sha384(text_bytes).hexdigest(),
            'SHA512': hashlib.sha512(text_bytes).hexdigest(),
            'SHA3-224': hashlib.sha3_224(text_bytes).hexdigest(),
            'SHA3-256': hashlib.sha3_256(text_bytes).hexdigest(),
            'SHA3-384': hashlib.sha3_384(text_bytes).hexdigest(),
            'SHA3-512': hashlib.sha3_512(text_bytes).hexdigest(),
            'BLAKE2b': hashlib.blake2b(text_bytes).hexdigest(),
            'BLAKE2s': hashlib.blake2s(text_bytes).hexdigest(),
        }
        
        for name, hash_value in hashes.items():
            print(f"\033[93m{name:<10}\033[0m: {hash_value}")
        
        print("="*60)
        return hashes
    
    @staticmethod
    def hash_file(filepath, algorithm='sha256'):
        """Generate hash dari file"""
        try:
            if not os.path.exists(filepath):
                print(f"\n\033[91m❌ File not found: {filepath}\033[0m")
                return None
            
            # Pilih algoritma
            if algorithm.lower() == 'md5':
                hasher = hashlib.md5()
            elif algorithm.lower() == 'sha1':
                hasher = hashlib.sha1()
            elif algorithm.lower() == 'sha256':
                hasher = hashlib.sha256()
            elif algorithm.lower() == 'sha512':
                hasher = hashlib.sha512()
            else:
                print(f"\n\033[91m❌ Unsupported algorithm: {algorithm}\033[0m")
                return None
            
            # Baca file dalam chunks untuk file besar
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b''):
                    hasher.update(chunk)
            
            hash_value = hasher.hexdigest()
            print(f"\n\033[92m✅ File: {filepath}\033[0m")
            print(f"\033[93m{algorithm.upper()}\033[0m: {hash_value}")
            return hash_value
            
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def verify_hash(text, expected_hash, algorithm='sha256'):
        """Verifikasi hash dari text"""
        if not text or not expected_hash:
            print("\n\033[91m❌ Text and hash cannot be empty!\033[0m")
            return False
        
        try:
            # Pilih algoritma
            if algorithm.lower() == 'md5':
                computed_hash = hashlib.md5(text.encode()).hexdigest()
            elif algorithm.lower() == 'sha1':
                computed_hash = hashlib.sha1(text.encode()).hexdigest()
            elif algorithm.lower() == 'sha256':
                computed_hash = hashlib.sha256(text.encode()).hexdigest()
            elif algorithm.lower() == 'sha512':
                computed_hash = hashlib.sha512(text.encode()).hexdigest()
            else:
                print(f"\n\033[91m❌ Unsupported algorithm: {algorithm}\033[0m")
                return False
            
            if computed_hash == expected_hash.lower():
                print(f"\n\033[92m✅ Hash VERIFIED! Match found.\033[0m")
                return True
            else:
                print(f"\n\033[91m❌ Hash NOT verified! Mismatch.\033[0m")
                print(f"\033[90mComputed: {computed_hash}\033[0m")
                print(f"\033[90mExpected: {expected_hash}\033[0m")
                return False
                
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return False
    
    @staticmethod
    def simple_hash(text, algorithm='sha256'):
        """Generate single hash ( lebih sederhana )"""
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        
        hash_funcs = {
            'md5': hashlib.md5,
            'sha1': hashlib.sha1,
            'sha256': hashlib.sha256,
            'sha512': hashlib.sha512
        }
        
        if algorithm.lower() not in hash_funcs:
            print(f"\n\033[91m❌ Algorithm must be one of: {', '.join(hash_funcs.keys())}\033[0m")
            return None
        
        hash_value = hash_funcs[algorithm.lower()](text.encode()).hexdigest()
        print(f"\n\033[92m✅ {algorithm.upper()} hash: {hash_value}\033[0m")
        return hash_value
    
    @staticmethod
    def hash_with_salt(text, salt=None, algorithm='sha256'):
        """Hash dengan salt (untuk password)"""
        if not text:
            print("\n\033[91m❌ Text cannot be empty!\033[0m")
            return None
        
        # Generate salt jika tidak disediakan
        if salt is None:
            salt = os.urandom(32).hex()
        
        # Gabungkan text dengan salt
        salted_text = text + salt
        
        # Hash
        if algorithm.lower() == 'md5':
            hash_value = hashlib.md5(salted_text.encode()).hexdigest()
        elif algorithm.lower() == 'sha256':
            hash_value = hashlib.sha256(salted_text.encode()).hexdigest()
        elif algorithm.lower() == 'sha512':
            hash_value = hashlib.sha512(salted_text.encode()).hexdigest()
        else:
            print(f"\n\033[91m❌ Unsupported algorithm: {algorithm}\033[0m")
            return None
        
        print(f"\n\033[92m✅ Salted Hash ({algorithm.upper()})\033[0m")
        print(f"\033[93mSalt\033[0m : {salt}")
        print(f"\033[93mHash\033[0m: {hash_value}")
        
        return {'hash': hash_value, 'salt': salt}
    
    @staticmethod
    def verify_salted_hash(text, salt, expected_hash, algorithm='sha256'):
        """Verifikasi salted hash"""
        if not text or not salt or not expected_hash:
            print("\n\033[91m❌ Text, salt, and hash cannot be empty!\033[0m")
            return False
        
        salted_text = text + salt
        
        if algorithm.lower() == 'md5':
            computed_hash = hashlib.md5(salted_text.encode()).hexdigest()
        elif algorithm.lower() == 'sha256':
            computed_hash = hashlib.sha256(salted_text.encode()).hexdigest()
        elif algorithm.lower() == 'sha512':
            computed_hash = hashlib.sha512(salted_text.encode()).hexdigest()
        else:
            print(f"\n\033[91m❌ Unsupported algorithm: {algorithm}\033[0m")
            return False
        
        if computed_hash == expected_hash:
            print(f"\n\033[92m✅ Salted hash VERIFIED!\033[0m")
            return True
        else:
            print(f"\n\033[91m❌ Salted hash NOT verified!\033[0m")
            return False
    
    @staticmethod
    def compare_hashes(hash1, hash2):
        """Bandingkan dua hash"""
        if not hash1 or not hash2:
            print("\n\033[91m❌ Both hashes are required!\033[0m")
            return False
        
        if hash1 == hash2:
            print(f"\n\033[92m✅ Hashes MATCH!\033[0m")
            return True
        else:
            print(f"\n\033[91m❌ Hashes DO NOT match!\033[0m")
            return False
EOF
