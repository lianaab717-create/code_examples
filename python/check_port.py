import socket
import sys

def check_port(host, port):
    s = socket.socket()
    s.settimeout(3)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])

    if check_port(host, port):
        print(f"{host}:{port} is OPEN ✅")
    else:
        print(f"{host}:{port} is CLOSED ❌")
