from urllib.parse import urlparse

def validate_url(url):
    parsed = urlparse(url)
    return all([parsed.scheme, parsed.netloc])
