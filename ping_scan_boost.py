#!user/bin/python3

R="\033[1;31m"; #Red
Y="\033[1;33m"; #Yellow
C="\033[1;36m"; #Cyan
W="\033[0m"     #white

import ipaddress,subprocess,queue,threading,time

def scan_ip_address():
    while not q.empty():
        ip = q.get()
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
        q.task_done()

network     = input(f"{R}[+] Network to be scanned :{C}")
num_threads = input(f"{R}[+] Number of threads :{C}")

start_time = time.time()
print(f'''\n{Y}Starting scan...{W}''')
try:
    IP_Addresses = ipaddress.IPv4Network(network)       # get all IP address inside the network

    #initialize queue object that will be used by threads: (threads are going to get IP addresses from the queue)
    q = queue.Queue()

    # fill the queue with IP Addresses
    for ip in IP_Addresses:
        q.put(ip)           # the function put() will add an ip address to the queue in every iteration of the for loop

    for thread in range (int(num_threads)):
        threading.Thread(target=scan_ip_address).start()        # creatre and start a new thread that will execute the function scan_ip_address
    q.join()

except Exception as e:
    print("Exception ",e)

print(f"Execution time: {C}{time.time() - start_time}{W} seconds")
