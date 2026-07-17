#!user/bin/python3

R="\033[1;31m"; #Red
Y="\033[1;33m"; #Yellow
C="\033[1;36m"; #Cyan
W="\033[0m"     #white

import ipaddress
import subprocess

network= "0.0.0.0/24"
IP_Addresses = ipaddress.IPv4Network(network)
for ip in IP_Addresses:
    command = "ping -c 1 -w 1 {}".format(ip)
    process = subprocess.run(command,
            shell  = True,                       # use a real shell
            stdout = subprocess.PIPE,            # send standard output to a pipe
            stderr = subprocess.PIPE,            # send standard errors to a pipe
    )

    # check exit code to disvocer if a given ip address is reachable or not 
    if process.returncode == 0:
        print(f"ip address is reachable     : {C}{ip}{W}")
    else:
        print(f"ip address is not reachable : {R}{ip}{W}")
