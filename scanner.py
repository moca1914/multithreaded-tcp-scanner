import socket
import sys
import threading
from queue import Queue
import time

print("-" * 50)
print("   Custom Python Multi-threaded Port Scanner   ")
print("-" * 50)

target = input("Enter target IP or Domain: ")
start_port = int(input("Enter starting port (e.g., 1): "))
end_port = int(input("Enter ending port (e.g., 1024): "))

try:
    target_ip = socket.gethostbyname(target)
    print(f"\n[+] Scanning target: {target_ip}")
except socket.gaierror:
    print("\n[-] Error: Could not resolve hostname.")
    sys.exit()

print_lock = threading.Lock()


def scan_port(port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(1.0)

    try:
        result = s.connect_ex((target_ip, port))

        if result == 0:
            with print_lock:
                print(f" [✔] Port {port:5} is OPEN")
        s.close()
    except Exception:
        pass


def threader():
    while True:
        port = port_queue.get()
        scan_port(port)
        port_queue.task_done()


port_queue = Queue()

start_time = time.time()

num_threads = 100
for _ in range(num_threads):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for port in range(start_port, end_port + 1):
    port_queue.put(port)

port_queue.join()

end_time = time.time()
print("-" * 50)
print(f"[+] Scan completed in {end_time - start_time:.2f} seconds!")
print("-" * 50)
