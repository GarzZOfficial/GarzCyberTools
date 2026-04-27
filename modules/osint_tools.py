import socket
import dns.resolver
import requests

class OsintTools:
    @staticmethod
    def dns_lookup(domain):
        print(f"\n🔍 DNS Lookup untuk {domain}")
        print("="*40)
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']
        
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                print(f"\n{record} Records:")
                for answer in answers:
                    print(f"  → {answer}")
            except:
                print(f"\n{record} Records: Tidak ditemukan")
    
    @staticmethod
    def whois_lookup(domain):
        print(f"\n🔍 WHOIS Lookup untuk {domain}")
        print("="*40)
        
        try:
            import whois
            w = whois.whois(domain)
            
            print(f"Domain: {w.domain_name}")
            print(f"Registrar: {w.registrar}")
            print(f"Creation Date: {w.creation_date}")
            print(f"Expiration Date: {w.expiration_date}")
            print(f"Name Servers: {w.name_servers}")
        except ImportError:
            print("❌ Module 'python-whois' tidak terinstall!")
            print("Install dengan: pip install python-whois")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    @staticmethod
    def find_subdomains(domain):
        print(f"\n🔍 Mencari subdomain untuk {domain}")
        print("="*40)
        
        # Common subdomains
        subdomains = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 
                      'pop', 'ns1', 'webdisk', 'ns2', 'cpanel', 'whm', 
                      'autodiscover', 'autoconfig', 'api', 'blog', 'shop']
        
        found = []
        for sub in subdomains:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                found.append(subdomain)
                print(f"✅ {subdomain} → {ip}")
            except:
                pass
        
        print(f"\n📊 Ditemukan {len(found)} subdomain")
        return found
