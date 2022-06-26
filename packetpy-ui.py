#// PacketPy Main interactive script
#// https://github.com/fortless/PacketPy
import os
import time as t
import socket as sock

version = '1.1-01_beta' # Don't touch this

print("PacketPy version " + str(version))
print("Interactive script")
print("")
print("Please choose one of the following categories:")
print("")
print("----------------")
print("[1] ICMP tests")
print("[2] TCP tests")
print("[3] UDP tests")
print("[4] HTTP tests")
print("[99] Exit")
print("----------------")
category = input(">> ")
if int(category) == 1:
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
if int(category) == 99:
	print("Exiting PacketPy..")
	exit()
if int(category) == 2:
	print("")
	print("Please select a payload type:")
	print("--TCP tests--")
	print("[1] TCP SYN")
	print("[2] TCP SYN (Spoofed)")
	print("[99] Exit")
	tcptype = input(">> ")
	if int(tcptype) == 1:
		os.system("python3 payloads/tcp-syn.py")
	if int(tcptype) == 2:
	       	os.system("python3 payloads/tcp-syn-spoofed.py")
	if int(tcptype) == 99:
		print("Exiting PacketPy...")
		exit()
if int(category) == 3:
	print("")
	print("Please select a payload type:")
	print("--UDP tests--")
	print("[1] UDP Raw")
	print("[99] Exit")
	udptype = input(">> ")
	if int(udptype) == 1:
		os.system("python3 payloads/udp-raw.py")
	if int(udptype) == 99:
		print("Exiting PacketPy..")
		exit()
if int(category) == 4:
	print("")
	print("Please select a payload type:")
	print("--HTTP tests--")
	print("[1] HTTP-GET")
	print("[2] HTTP-POST")
	print("[99] Exit")
	httptype = input(">> ")
	if int(httptype) == 1:
		os.system("python3 payloads/http-get.py")
	if int(httptype) == 2:
		os.system("python3 payloads/http-post.py")
	if int(httptype) == 99:
		print("Exiting PacketPy..")
		exit()
