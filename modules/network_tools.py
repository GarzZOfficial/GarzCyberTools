cat > modules/network_tools.py << 'EOF'
import socket
import subprocess

class NetworkTools:
    @staticmethod
    def port_scanner(target):
        print(f"\n\033[93m🔍 Scanning {target}...\033[0m")
        common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 8080]
        
        open_ports = []
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"\033[92m✅ Port {port} OPEN\033[0m")
            sock.close()
        
        print(f"\n\033[93m📊 Total open ports: {len(open_ports)}\033[0m")
    
    @staticmethod
    def get_ip_info(target):
        try:
            import requests
            ip = socket.gethostbyname(target)
            print(f"\n\033[92m🌐 IP Address: {ip}\033[0m")
            
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            
            if data['status'] == 'success':
                print(f"📍 Country: {data['country']}")
                print(f"🏙️ City: {data['city']}")
                print(f"📡 ISP: {data.get('isp', 'N/A')}")
                print(f"🗺️ Coordinates: {data['lat']}, {data['lon']}")
        except ImportError:
            print("\n\033[91m❌ Install requests: pip install requests\033[0m")
        except Exception as e:
            print(f"\n\033[91m❌ Error: {e}\033[0m")
EOF
