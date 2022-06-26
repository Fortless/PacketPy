#// PacketPy Main interactive script
#// https://github.com/fortless/PacketPy
import os
import time as t
import socket as sock


version = '1.1-01_beta' # Don't touch this

def clearterminal():
	if os.name == 'nt':
		os.system("cls")
	elif os.name != 'nt':
		os.system("clear")


clearterminal()

print("PacketPy version " + str(version))
print("Interactive script")
print("")
print("Welcome to PacketPy!")

loop = False
while True:
	if loop == True:
		print("")
		print("---")
		print("[1] Return to main menu")
		print("[99] Exit")
		print("---")
		loopdecision = input(">> ")
		if loopdecision == str("99"):
			exit
		if loopdecision != str("1"):
			print("Invalid selection, assuming 1")
	print("")
	print("Please select a menu")
	print("----------------")
	print("[1] ICMP tests")
	print("[2] TCP tests")
	print("[3] UDP tests")
	print("[4] HTTP tests")
	print("")
	print("[98] Help")
	print("[99] Exit")
	print("----------------")
	category = input(">> ")
	loop = True
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
		clearterminal()
		print("")
		print("Exiting PacketPy.. Goodbye!")
		print("")
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
	if int(category) == 98:
		clearterminal()
		print("--- PacketPy Help ---")
		print("")
		print("PacketPy is an open source framework for")
		print("stress testing network services, made in")
		print("Python. It is written with stability and")
		print("ease of use in mind, which means anybody")
		print("can use it against networks with granted")
		print("permission to use it.")
		print("")
		print("It currently features 4 main payload vectors,")
		print("mainly ICMP, TCP, UDP, HTTP, and accesible via")
		print("the on-screen menu.")
		print("")
		print("We reccomend running PacketPy as root, because")
		print("raw sockets require root privileges to work.")
		print("")
		print("--- PacketPy Help ---")
