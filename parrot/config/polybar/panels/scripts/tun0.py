#!/usr/bin/python3
import re
import subprocess

# Getting IPs and saving them in a file
with open('ip.txt', 'w') as f:
    subprocess.run(['ip', 'a'], stdout=f, text=True)

# Finding tun0 IP
with open('ip.txt', 'r') as txt_file:
    IP = txt_file.read()

# Regular expression pattern
pattern = re.compile(r'\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
search_tun0 = pattern.findall(IP)

if search_tun0:
    # Print the first matched IP address
    tun0_IP = search_tun0[0]
    print(tun0_IP)
else:
    print("offline")
