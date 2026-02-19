import ssl
import socket
from urllib.parse import urlparse
from datetime import datetime

def check_ssl(url):
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname

        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()

        expiry_date = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
        days_left = (expiry_date - datetime.utcnow()).days

        return {
            "issuer": dict(x[0] for x in cert['issuer']),
            "expiry_date": expiry_date.strftime("%Y-%m-%d"),
            "days_left": days_left
        }

    except Exception as e:
        return {"error": str(e)}
