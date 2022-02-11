# PacketPy
## About
PacketPy is an open-source solution for stress testing network devices using different testing methods.
Currently, there are only two categories out of three availible, out of which ICMP and UDP.
=========
## Payloads

### ICMP
ICMP payloads can vary from randomized byte size, spoofed source address and more, and I have included the following:
1. ICMP-Fixed, this has the same payload each time
2. ICMP-Linear, this will increase the payload by 1 byte each packet
3. ICMP-Randomized, this will 

### UDP
UDP payloads can also vary by destination port and source port, of which the *source* port can be spoofed, as well as the *source* ***IP***.
Currently, there is only one payload that I have coded in the past, that being *UDP-Raw*.
It can send raw packets as fast as the NIC can send.
