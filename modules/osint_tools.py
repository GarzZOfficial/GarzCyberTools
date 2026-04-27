cat > modules/osint_tools.py << 'EOF'
import socket
import dns.resolver

class OsintTools:
    @staticmethod
    def dns_lookup(domain):
        print(f"\n\033[93m🔍 DNS Lookup untuk {domain}\033[0m")
        print("="*40)
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT']
        
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                print(f"\n\033[92m{record} Records:\033[0m")
                for answer in answers:
                    print(f"  → {answer}")
            except:
                print(f"\n\033[91m{record} Records: Tidak ditemukan\033[0m")
EOF
