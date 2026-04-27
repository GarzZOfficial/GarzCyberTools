cat > modules/osint_tools.py << 'EOF'
import socket

class OsintTools:
    @staticmethod
    def dns_lookup(domain):
        try:
            ip = socket.gethostbyname(domain)
            print(f"\n\033[92m🌐 Domain: {domain}\033[0m")
            print(f"📍 IP Address: {ip}")
        except:
            print("\n\033[91m❌ Gagal resolve domain!\033[0m")
EOF
