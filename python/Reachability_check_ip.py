import subprocess
import sys

def check_ip(ip):
    result = subprocess.run(
        ["ping", "-c", "1", ip],
        stdout=subprocess.DEVNULL
    )
    return result.returncode == 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_ip.py <IP>")
        sys.exit(1)

    ip = sys.argv[1]

    if check_ip(ip):
        print(f"{ip} is reachable ✅")
    else:
        print(f"{ip} is NOT reachable ❌")

# python3 check_ip.py 8.8.8.8