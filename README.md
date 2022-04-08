# PacketPy
## About
> PacketPy is an open-source solution for stress testing network devices using different testing methods.
> Currently, there are only two categories out of three availible, out of which ICMP and UDP.
***
# How to run
> > First, clone the repository
> > Second, make sure you have all the dependencies installed, listed at the bottom of this page
> > Third, go into the repository and run `python3 packetpy-ui.py`
> > Enjoy!


## Payloads
* * *
### ICMP
ICMP payloads can vary from randomized byte size, spoofed source address and more, and I have included the following:
1. ICMP-Fixed, this has the same payload each time
2. ICMP-Linear, this will increase the payload by 1 byte each packet
3. ICMP-Randomized, this will 
* * *
### UDP
UDP payloads can also vary by destination port and source port, of which the *source* port can be spoofed, as well as the *source* ***IP***.
Currently, there is only one payload that I have coded in the past, that being *UDP-Raw*.
It can send raw packets as fast as the NIC can send.
* * *
### TCP
TCP payloads can overwhelm certain applications running behind a TCP port. One way to abuse the TCP protocol is by sending so many **SYN** requests
so that the recieving end cannot handle that many connections.
For IDS/IPS evasion, I've also built in another payload where you can select what source IPv4 to use for outgoint **SYN** requests, but it needs to
be run with equivelent permissions so that Python can create a raw socket in order to *spoof* the IP.
Currently, this payload is limited by single thread performance.
* * *
### HTTP
HTTP payloads are layer 7 payloads that overwhelms websites by sending many GET / POST requests to the HTTP server.
* * *
## Requirements and Dependencies
**For Windows 7 and later**, you need Npcap or Winpcap, Requests, which can be installd with `pip install requests` , and Scapy, which can be installed with `pip install scapy`.

**For Linux**, you need to install Scapy, which can be installed with `pip install scapy`, and Requests, which can be installed with `pip install requests`.


###### Made with ❤️ from Ukraine and Romania
