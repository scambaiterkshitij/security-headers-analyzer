import requests
from config import SECURITY_HEADERS

def analyze_headers(url):
    try:
        response = requests.get(url, timeout=5)
        results = {}

        for header in SECURITY_HEADERS:
            results[header] = header in response.headers

        server_info = response.headers.get("Server", "Not Disclosed")

        return results, server_info

    except requests.exceptions.RequestException as e:
        return None, str(e)
