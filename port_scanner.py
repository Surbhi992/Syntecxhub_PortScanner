import socket
import threading

print("=== Simple Port Scanner ===")

target = input("Enter target IP or domain: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

open_ports = []

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        s.close()
    except:
        pass

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan Complete!")
print("Open Ports:", open_ports)

with open("scan_results.txt", "w") as file:
    file.write(f"Target: {target}\n")
    file.write(f"Open Ports: {open_ports}\n")

print("\nResults saved in scan_results.txt")
