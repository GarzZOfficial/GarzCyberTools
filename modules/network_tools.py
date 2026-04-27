cat > modules/network_tools.py << 'EOF'
import socket

class NetworkTools:
    @staticmethod
    def port_scanner(target):
        print(f"\n\033[93m🔍 Scanning {target}...\033[0m")
        ports = [21, 22, 23, 25, 53, 80, 443, 8080]
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            if sock.connect_ex((target, port)) == 0:
                print(f"\033[92m✅ Port {port} OPEN\033[0m")
            sock.close()
EOF
