import socket
import requests

def resolve_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"[+] IP Address: {ip}")
    except:
        print("[-] Could not resolve IP")

def check_status(domain):
    try:
        res = requests.get(f"http://{domain}", timeout=5)
        print(f"[+] HTTP Status: {res.status_code}")
    except:
        print("[-] Site not reachable")

def port_scan(domain):
    print("[*] Scanning common ports...")
    ports = [21, 22, 80, 443, 8080]
    for port in ports:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect((domain, port))
            print(f"[OPEN] Port {port}")
        except:
            pass
        s.close()

def subdomain_check(domain):
    subs = ["www", "mail", "ftp", "dev", "test"]
    print("[*] Checking subdomains...")
    for sub in subs:
        url = f"{sub}.{domain}"
        try:
            socket.gethostbyname(url)
            print(f"[FOUND] {url}")
        except:
            pass

if __name__ == "__main__":
    target = input("Enter target domain: ")

    print("\n--- ReconX Scan Started ---\n")

    resolve_ip(target)
    check_status(target)
    port_scan(target)
    subdomain_check(target)

    print("\n--- Scan Complete ---")
