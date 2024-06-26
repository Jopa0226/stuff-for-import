#modules for scanning
import socket

#modules for general tasks
import time
import os
import sys

#clear the screen based os OS
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

#display Python version and current time.
print("Python {0:s} on {1:s}".format(sys.version, sys.platform))
print("Current time: {0:s}".format(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())))

#get host details for script
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print(host_name, host_ip)

#dictionary storing known port number details
port_info = { 20: "FTP Protocol (data)", 21:"FTP Protocol (control)", 25: "Simple Mail Transfer Protocol",
              53: "Domain Name Service", 67: "Dynamic Host Configuration Protocol (server)", 
              68: "Dynamic Host Configuration Protocol (client)", 69: "Trivial File Transfer Protocol",
              80: "Hypertext Transfer Protocol", 110: "Post Office Protocol Version 3",
              135:"Microsoft RPC Locator Service", 139:"NetBIOS Session Service",
              443:"Hypertext Transfer Protocol Secure"}

#function that performs the scan
def check_ports(host_to_scan, port_to_scan,port_info):
    scanner = socket.socket()
    scanner.settimeout(0.5)
    connected = scanner.connect_ex((host_to_scan, port_to_scan))

    if connected == 0:
        if port_to_scan in port_info:
            print("Host:",host_to_scan, "Port:", port_to_scan, port_info[port_to_scan],"is open.")
        else:
            print("Host:",host_to_scan, "Port:", port_to_scan, "is open.")
        scanner.close()
    else:
        print("Host:",host_to_scan, "Port:", port_to_scan, "is not open.")

#get network details for the scan
#you will need to ensure that a valid network ID is entered
host = input("Enter network ID: ")
host_parts = host.split(".")
host_parts = [int(host_part) for host_part in host_parts]

#range usually to 255
#set to scan every second host for testing
for host_end in range (20,24,2):
    host_to_scan = str(host_parts[0]) + "." + str(host_parts[1]) + '.' + str(host_parts[2]) + '.' + str(host_end)
    
    # adjust port range to match scanning needs
    for port in range(20, 139):
        check_ports(host_to_scan,port,port_info)

