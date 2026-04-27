cat > modules/__init__.py << 'EOF'
from .hasher import HashTools
from .encoder import EncoderTools
from .password_checker import PasswordTools
from .crypto_tools import CryptoTools
from .network_tools import NetworkTools
from .osint_tools import OsintTools
EOF
