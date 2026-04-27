import socket
import subprocess
import platform
import requests

class NetworkTools:
    @staticmethod
    def port_scanner(target):
        print(f"\n🔍 Scanning {target}...")
        common_ports = [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 
                        143, 443, 445, 993, 995, 1723, 3306, 3389, 
                        5900, 8080]
        
        open_ports = []
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"✅ Port {port} OPEN")
            sock.close()
        
        print(f"\n📊 Total open ports: {len(open_ports)}")
        return open_ports
    
    @staticmethod
    def ping_sweep(network):
        print(f"\n🔍 Scanning network {network}.0/24...")
        live_hosts = []
        
        for i in range(1, 255):
            ip = f"{network}.{i}"
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '1', ip]
            
            try:
                result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if result.returncode == 0:
                    live_hosts.append(ip)
                    print(f"✅ {ip} is alive")
            except:
                pass
        
        print(f"\n📊 Live hosts: {len(live_hosts)}")
        return live_hosts
    
    @staticmethod
    def get_ip_info(target):
        try:
            # Resolve domain to IP
            ip = socket.gethostbyname(target)
            print(f"\n🌐 IP Address: {ip}")
            
            # Get IP info from ip-api.com
            response = requests.get(f"http://ip-api.com/json/{ip}")
            data = response.json()
            
            if data['status'] == 'success':
                print(f"📍 Country: {data['country']}")
                print(f"🏙️ City: {data['city']}")
                print(f"📡 ISP: {data['isp']}")
                print(f"🗺️ Coordinates: {data['lat']}, {data['lon']}")
                print(f"📮 ZIP Code: {data['zip']}")
                print(f"🌍 Timezone: {data['timezone']}")
            else:
                print("❌ Tidak bisa mendapatkan informasi detail")
        except Exception as e:
            print(f"❌ Error: {e}")
