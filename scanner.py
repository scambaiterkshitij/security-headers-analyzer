import requests

def check_headers(url):
    try:
        response = requests.get(url, timeout=5)
        headers = response.headers

        print(f"\nScanning: {url}\n")

        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security",
            "X-Content-Type-Options"
        ]

        for header in security_headers:
            if header in headers:
                print(f"[+] {header} Found")
            else:
                print(f"[-] {header} Missing")

        print("\nServer Info:", headers.get("Server", "Not Disclosed"))

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    target = input("Enter target URL (with https://): ")
    check_headers(target)
