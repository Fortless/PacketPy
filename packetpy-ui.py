# PacketPy Main interactive script
# https://github.com/fortless/PacketPy
import os
import time as t
import socket as sock

version = '1.0-07_beta'

print("PacketPy version " + str(version))
print("Interactive script")
print("")
print("Please choose one of the following categories:")
print("")
print("----------------")
print("[1] ICMP tests")
print("[2] TCP tests")
print("[3] UDP tests")
print("[99] Exit")
print("----------------")
category = input(">> ")
if int(category) == 1:
	icmptype = '3'
	print("")
	print("Please select a payload type:")
	print("--ICMP tests--")
	print("[1] Fixed ICMP")
	print("[2] Linear ICMP")
	print("[3] Randomized ICMP")
	print("[99] Exit")
	print("--------------")
	icmptype = input(">> ")
	if int(icmptype) == 1:
		os.system("python3 payloads/icmp-fixed.py")
	if int(icmptype) == 2:
		os.system("python3 payloads/icmp-linear.py")
	if int(icmptype) == 3:
		os.system("python3 payloads/icmp-randomized.py")
	if int(icmptype) == 99:
		print("Exiting PacketPy..")
		exit()
if int(category) == 2:
	print("This payload is work in progress.")
if int(category) == 3:
	print("This payload is work in progress.")
if int(category) == 99:
	print("Exiting PacketPy..")
	exit()
