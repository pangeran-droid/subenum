import requests
import socket
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

THREADS = 30
TIMEOUT = 15

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
}

session = requests.Session()
session.headers.update(HEADERS)

def banner():
    print("\033[96m")
    print(r"""
               __                             
   _______  __/ /_  ___  ____  __  ______ ___ 
  / ___/ / / / __ \/ _ \/ __ \/ / / / __ `__ \
 (__  ) /_/ / /_/ /  __/ / / / /_/ / / / / / /
/____/\__,_/_.___/\___/_/ /_/\__,_/_/ /_/ /_/ 
                                              
Simple Subdomain Enumerator
""")
    print("\033[0m")


def source_crt(domain):
    results = set()
    try:
        r = session.get(f"https://crt.sh/?q=%25.{domain}&output=json", timeout=TIMEOUT)
        data = r.json()
        for item in data:
            for sub in item.get("name_value", "").split("\n"):
                if sub.endswith(domain):
                    results.add(sub.lower())
    except:
        pass
    return results


def source_bufferover(domain):
    results = set()
    try:
        r = session.get(f"https://dns.bufferover.run/dns?q=.{domain}", timeout=TIMEOUT)
        data = r.json()
        for entry in data.get("FDNS_A", []):
            sub = entry.split(",")[1]
            if sub.endswith(domain):
                results.add(sub.lower())
    except:
        pass
    return results


def source_hackertarget(domain):
    results = set()
    try:
        r = session.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", timeout=TIMEOUT)
        for line in r.text.splitlines():
            sub = line.split(",")[0]
            if sub.endswith(domain):
                results.add(sub.lower())
    except:
        pass
    return results


def resolve_host(host):
    try:
        socket.getaddrinfo(host, None, socket.AF_INET)
        return True
    except:
        return False


def check_status(host):
    for proto in ["https://", "http://"]:
        try:
            r = session.get(proto + host, timeout=10, allow_redirects=True, verify=False)
            return r.status_code
        except:
            continue
    return None


def main():
    banner()
    parser = argparse.ArgumentParser(description="Simple Subdomain Enumerator")
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("--status", action="store_true", help="Show HTTP status")
    args = parser.parse_args()

    domain = args.domain.strip()

    sources = [source_crt, source_bufferover, source_hackertarget]
    all_subs = set()

    for src in sources:
        all_subs.update(src(domain))

    if not all_subs:
        return

    live_hosts = []
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = {executor.submit(resolve_host, sub): sub for sub in all_subs}
        for future in as_completed(futures):
            host = futures[future]
            if future.result():
                live_hosts.append(host)

    live_hosts = sorted(live_hosts)

    if args.status:
        with ThreadPoolExecutor(max_workers=THREADS) as executor:
            futures = {executor.submit(check_status, host): host for host in live_hosts}
            for future in as_completed(futures):
                host = futures[future]
                status = future.result()
                if status:
                    print(f"{host} [{status}]")
                else:
                    print(host)
    else:
        for host in live_hosts:
            print(host)


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    main()
