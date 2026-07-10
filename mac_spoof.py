#!/usr/bin/python3
import random,subprocess

# color codes 
R="\033[1;31m"; #Red
Y="\033[1;33m"; #Yellow
C="\033[1;36m"; #Cyan
W="\033[0m";     #white

# generate a new mac address
random_mac = [0x00,0x50,0x56, random.randint(0x00,0x7f),random.randint(0x00,0xff),random.randint(0x00,0xff)]
mac_addr   = ":".join(map(lambda x: "%02x" %x,random_mac))
print(R,"New MAC address:",C,mac_addr,W)

# OLD MAC address:
print(R,"OLD MAC adress:",W)
subprocess.call(["ip","link","show","eth0"])

## Change the MAC of NIC
subprocess.call(["ifdown","eth0"])                              # step1 : disconnect from the LAN : ifdown <NIC NAME>
subprocess.call(["ip","link","set","eth0","down"])              # step2 : deactivate the NIC
subprocess.call(["ip","link","set","eth0","address",mac_addr])  # step3 : change MAC address
subprocess.call(["ip","link","set","eth0","up"])                # step4 : activate again the MAC address

print(C,"NEW MAC address:",W)
subprocess.call(["ip","link","show","eth0"])                    # step5 : check the new MAC address

print("\n")

# connect again to the LAN
