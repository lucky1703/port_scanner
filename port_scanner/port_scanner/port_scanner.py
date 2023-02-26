import socket
import ipaddress

while True:
    target = input("Enter the host to scan (IPv4 address only): ")
    try:
        ipaddress.IPv4Address(target)
        break
    except ipaddress.AddressValueError:
        print("Invalid IPv4 address. Please try again.")

min_port = int(input("Enter the minimum port number: "))
max_port = int(input("Enter the maximum port number: "))

print(f"Scanning {target} from port {min_port} to {max_port}...")

for port in range(min_port, max_port+1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f"Port {port} is open")
    s.close()

