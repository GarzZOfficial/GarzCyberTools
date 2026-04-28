cat > modules/__init__.py << 'EOF'
"""
Security Tools Package
Collection of security, cryptography, and OSINT tools
"""

# Import semua tools
from .hasher import HashTools
from .encoder import EncoderTools
from .crypto_tools import CryptoTools
from .password_checker import PasswordTools
from .network_tools import NetworkTools
from .osint_tools import OsintTools
from .steganography import StegoTools
from .forensic_tools import ForensicTools

# Package metadata
__version__ = "1.0.0"
__author__ = "Security Tools"
__description__ = "A comprehensive security tools package"

# Daftar semua modules yang tersedia
__all__ = [
    'HashTools',
    'EncoderTools', 
    'CryptoTools',
    'PasswordTools',
    'NetworkTools',
    'OsintTools',
    'StegoTools',
    'ForensicTools'
]

# Package initialization
print(f"\033[92m🔐 Security Tools Package v{__version__} loaded\033[0m")
print(f"\033[90mAvailable modules: {', '.join(__all__)}\033[0m\n")
EOF
