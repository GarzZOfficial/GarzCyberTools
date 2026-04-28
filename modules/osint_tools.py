cat > modules/osint_tools.py << 'EOF'
import socket
import requests
import json
import subprocess
import platform
from urllib.parse import urlparse

class OsintTools:
    @staticmethod
    def dns_lookup(domain):
        """DNS lookup untuk mendapatkan IP address"""
        try:
            # Clean domain from http:// or https://
            domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
            
            ip = socket.gethostbyname(domain)
            print(f"\n\033[92m🌐 Domain: {domain}\033[0m")
            print(f"📍 IP Address: {ip}")
            
            # Try to get all IPs (for load balancing)
            try:
                addrinfo = socket.getaddrinfo(domain, None)
                ips = set()
                for addr in addrinfo:
                    ips.add(addr[4][0])
                if len(ips) > 1:
                    print(f"📡 All IPs: {', '.join(ips)}")
            except:
                pass
            
            return ip
        except socket.gaierror:
            print(f"\n\033[91m❌ Gagal resolve domain: {domain}\033[0m")
            return None
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def reverse_dns(ip_address):
        """Reverse DNS lookup (IP to Domain)"""
        try:
            hostname = socket.gethostbyaddr(ip_address)
            print(f"\n\033[92m🔄 Reverse DNS for {ip_address}\033[0m")
            print(f"📍 Hostname: {hostname[0]}")
            return hostname[0]
        except socket.herror:
            print(f"\n\033[91m❌ No reverse DNS record for {ip_address}\033[0m")
            return None
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def get_geoip(ip=None):
        """Get geolocation information from IP address"""
        # Get public IP if none provided
        if ip is None:
            try:
                response = requests.get('https://api.ipify.org?format=json', timeout=5)
                ip = response.json()['ip']
                print(f"\n\033[93m🔍 Using your public IP: {ip}\033[0m")
            except:
                print("\n\033[91m❌ Could not detect your public IP\033[0m")
                return None
        
        try:
            # Using ip-api.com (free, no API key required)
            response = requests.get(f'http://ip-api.com/json/{ip}', timeout=10)
            data = response.json()
            
            if data['status'] == 'success':
                print(f"\n\033[92m📍 Geolocation for {ip}:\033[0m")
                print(f"  🌍 Country     : {data['country']} ({data['countryCode']})")
                print(f"  🏙️  Region      : {data['regionName']}")
                print(f"  🏛️  City        : {data['city']}")
                print(f"  📮 Postal Code : {data['zip']}")
                print(f"  📡 ISP         : {data['isp']}")
                print(f"  🏢 Organization: {data['org']}")
                print(f"  🌐 AS          : {data['as']}")
                print(f"  📍 Coordinates : {data['lat']}, {data['lon']}")
                print(f"  🗺️  Google Maps : https://maps.google.com/?q={data['lat']},{data['lon']}")
                return data
            else:
                print(f"\n\033[91m❌ Could not get geolocation for {ip}\033[0m")
                return None
        except requests.exceptions.RequestException as e:
            print(f"\n\033[91m❌ Network error: {e}\033[0m")
            return None
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def dns_records(domain, record_type='A'):
        """Get DNS records for a domain"""
        try:
            import dns.resolver
            
            # Clean domain
            domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
            
            # Valid record types
            valid_records = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA', 'PTR']
            
            if record_type.upper() not in valid_records:
                print(f"\n\033[91m❌ Invalid record type. Use: {', '.join(valid_records)}\033[0m")
                return None
            
            print(f"\n\033[92m📡 {record_type.upper()} records for {domain}:\033[0m")
            
            answers = dns.resolver.resolve(domain, record_type)
            records = []
            for answer in answers:
                print(f"  {answer}")
                records.append(str(answer))
            
            if not records:
                print(f"  No {record_type.upper()} records found")
            
            return records
            
        except ImportError:
            print("\n\033[91m❌ dnspython not installed. Run: pip install dnspython\033[0m")
            return None
        except dns.resolver.NoAnswer:
            print(f"  No {record_type.upper()} records found")
            return []
        except dns.resolver.NXDOMAIN:
            print(f"\n\033[91m❌ Domain {domain} does not exist\033[0m")
            return None
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
            return None
    
    @staticmethod
    def all_dns_records(domain):
        """Get all common DNS records for a domain"""
        domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
        
        print(f"\n\033[92m🔍 Complete DNS lookup for {domain}:\033[0m")
        print("="*50)
        
        record_types = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME', 'SOA']
        
        for record_type in record_types:
            print(f"\n\033[93m{record_type} Records:\033[0m")
            OsintTools.dns_records(domain, record_type)
    
    @staticmethod
    def email_validation(email):
        """Validate email format and check domain MX records"""
        import re
        
        # Email regex pattern
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        print(f"\n\033[92m📧 Email Analysis: {email}\033[0m")
        print("="*40)
        
        # Check format
        if re.match(email_regex, email):
            print(f"✅ Valid email format")
            domain = email.split('@')[1]
            print(f"📡 Domain: {domain}")
            
            # Check MX records
            try:
                import dns.resolver
                mx_records = dns.resolver.resolve(domain, 'MX')
                print(f"📮 MX Records found: {len(list(mx_records))}")
                print(f"  Email server exists")
                return True
            except ImportError:
                print("⚠️  dnspython not installed (pip install dnspython)")
                return True
            except:
                print(f"⚠️  Could not verify MX records for {domain}")
                return True
        else:
            print(f"❌ Invalid email format")
            return False
    
    @staticmethod
    def port_scan(host, ports=None):
        """Simple port scanner for OSINT"""
        if ports is None:
            # Common ports
            ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 
                    993, 995, 1433, 1723, 3306, 3389, 5432, 5900, 8080, 8443]
        
        print(f"\n\033[92m🔍 Scanning {host} for open ports...\033[0m")
        print("="*50)
        
        open_ports = []
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                service = OsintTools._get_service_name(port)
                print(f"✅ Port {port:5d}: OPEN    ({service})")
                open_ports.append(port)
            sock.close()
        
        if not open_ports:
            print("No open ports found")
        else:
            print(f"\n📊 Total open ports: {len(open_ports)}")
        
        return open_ports
    
    @staticmethod
    def _get_service_name(port):
        """Get common service name by port"""
        services = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP', 53: 'DNS',
            80: 'HTTP', 110: 'POP3', 135: 'RPC', 139: 'NetBIOS', 143: 'IMAP',
            443: 'HTTPS', 445: 'SMB', 993: 'IMAPS', 995: 'POP3S', 1433: 'MSSQL',
            1723: 'PPTP', 3306: 'MySQL', 3389: 'RDP', 5432: 'PostgreSQL',
            5900: 'VNC', 8080: 'HTTP-Alt', 8443: 'HTTPS-Alt'
        }
        return services.get(port, 'Unknown')
    
    @staticmethod
    def whois_lookup(domain):
        """Simple WHOIS lookup using whois library"""
        try:
            import whois
            
            domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
            
            print(f"\n\033[92m📋 WHOIS Information for {domain}:\033[0m")
            print("="*50)
            
            w = whois.whois(domain)
            
            if w.registrar:
                print(f"Registrar      : {w.registrar}")
            if w.creation_date:
                print(f"Creation Date  : {w.creation_date}")
            if w.expiration_date:
                print(f"Expiry Date    : {w.expiration_date}")
            if w.name_servers:
                print(f"Name Servers   : {', '.join(w.name_servers) if isinstance(w.name_servers, list) else w.name_servers}")
            if w.org:
                print(f"Organization   : {w.org}")
            if w.country:
                print(f"Country        : {w.country}")
            
            return w
            
        except ImportError:
            print("\n\033[91m❌ python-whois not installed. Run: pip install python-whois\033[0m")
            return None
        except Exception as e:
            print(f"\n\033[91m❌ WHOIS lookup failed: {e}\033[0m")
            return None
    
    @staticmethod
    def subdomain_scan(domain, wordlist=None):
        """Simple subdomain scanner"""
        if wordlist is None:
            # Common subdomains
            wordlist = [
                'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
                'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'ns', 'test', 'm',
                'imap', 'ns3', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news',
                'vpn', 'ns4', 'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile',
                'mx', 'static', 'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 'cp',
                'calendar', 'wiki', 'web', 'media', 'email', 'images', 'img', 'video',
                'download', 'dns', 'api', 'app', 'store', 'backup', 'manage'
            ]
        
        domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
        
        print(f"\n\033[92m🔍 Scanning subdomains for {domain}...\033[0m")
        print("="*50)
        
        found_subdomains = []
        
        for sub in wordlist:
            subdomain = f"{sub}.{domain}"
            try:
                ip = socket.gethostbyname(subdomain)
                print(f"✅ Found: {subdomain} -> {ip}")
                found_subdomains.append(subdomain)
            except socket.gaierror:
                pass
        
        print(f"\n📊 Total subdomains found: {len(found_subdomains)}")
        return found_subdomains
    
    @staticmethod
    def ip_info(ip):
        """Get comprehensive IP information"""
        print(f"\n\033[92m🖥️  IP Information for {ip}\033[0m")
        print("="*50)
        
        # Geolocation
        OsintTools.get_geoip(ip)
        
        # Reverse DNS
        print("\n\033[93mReverse DNS:\033[0m")
        OsintTools.reverse_dns(ip)
        
        return True
    
    @staticmethod
    def domain_info(domain):
        """Get comprehensive domain information"""
        domain = domain.replace('http://', '').replace('https://', '').split('/')[0]
        
        print(f"\n\033[92m🌐 Domain Information for {domain}\033[0m")
        print("="*60)
        
        # DNS Lookup
        print("\n\033[93mDNS Lookup:\033[0m")
        ip = OsintTools.dns_lookup(domain)
        
        if ip:
            # Geolocation
            print("\n\033[93mGeolocation:\033[0m")
            OsintTools.get_geoip(ip)
        
        # DNS Records
        print("\n\033[93mDNS Records:\033[0m")
        OsintTools.all_dns_records(domain)
        
        # WHOIS
        OsintTools.whois_lookup(domain)
        
        return True
EOF
