#!/usr/bin/python3

import scapy.all as scapy
import time

R="\033[1;31m"; #Red
Y="\033[1;33m"; #Yellow
C="\033[1;36m"; #Cyan
W="\033[0m"     #white


# construct the ARP Echo Request Packets
ether_req       = scapy.Ether()             # Ether header
ether_req.dst   = "ff:ff:ff:ff:ff:ff"       # broadcast MAC address
arp_req         = scapy.ARP()               # ARP header
arp_req.pdst    = "192.168.1.0/24"          # set the ip address or the LAN subnet to be scanned
ARP_Request_PKT = ether_req/arp_req         # complete ARP packet
print(R,"ARP Echo Request Packet Construction Complete",W)


# scanning the LAN
T1_SCAN_START = time.time()         # get the current time when scan is started
print(C,"Scan started",W)
ans = scapy.srp(ARP_Request_PKT,timeout=1,retry=1,verbose=False,iface="eth0",inter=0.005)[0]
T2_SCAN_COMPLETE = time.time() 
print("Time needed for the scan",R,T2_SCAN_COMPLETE - T1_SCAN_START,"seconds",W)

# get the live hosts
for snd,rcv in ans:
    print("Live Host:",C,rcv[0].psrc,W)
