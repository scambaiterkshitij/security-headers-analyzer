import json

def print_report(results, server_info):
    print("\nScan Results:\n")

    for header, status in results.items():
        if status:
            print(f"[+] {header} Found")
        else:
            print(f"[-] {header} Missing")

    print("\nServer Info:", server_info)


def save_json(results, server_info, filename="report.json"):
    data = {
        "headers": results,
        "server": server_info
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
