#!/usr/bin/python3
#a huge thank you and shoutout to stackoverflow my lord and savior <3
#feel free to clone this and use it during your CTF adventures.

import socket, sys, threading
from os import system, name

global verbosity 
verbosity = 0
def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def portscan(ip_addr,port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip_addr, port))
        if result == 0:
            print(f"Port {port} open on {ip_addr}")
        sock.close()

def beginScan(ip_addr,port_start,port_end,multihost_flag):
    multihost_flag = multihost_flag
    if multihost_flag == 0:
        if verbosity == 1:
            print(f"[+] Scanning Host: {ip_addr}")
        for port in range(int(port_start), int(port_end) + 1):
            t = threading.Thread(target=portscan,args=(ip_addr,port)) 
            t.start() 
        if verbosity == 1:
            print(f"[+] Scan on host {ip_addr} complete.")        
    elif multihost_flag == 1:
        for host_portion in range (1,255):
            ip_addr_m = ip_addr + "." + str(host_portion)
            
            if verbosity == 1:
                print(f"[+] Scanning {ip_addr_m} in range {ip_addr}.1/24")
            for port in range(int(port_start), int(port_end) + 1):
                t = threading.Thread(target=portscan,args=(ip_addr_m,port)) 
                t.start() 
            if verbosity == 1:    
                print(f"[+] Scan on host {ip_addr_m} complete.") 

if __name__ == '__main__':
    if sys.argv.__contains__("-v"):
        verbosity = 1
    if sys.argv.__contains__('-h'):
            clear()
            print(f"[+] Usage:\n[*]  Verbosity: -v\n[*]  Single Host Scan: -s\n [-]  e.g ./scanner.py <ip> <port_start> <port_end> -s\n [-]  e.g ./scanner.py 10.1.1.1 1 65535 -s\n[*]  Scan Multiple Hosts: -m\n [-]  e.g ./scanner.py <ip up to host portion> <port_start> <port_end> -m\n [-] e.g ./scanner.py 10.1.1 1 65535 -m\n[*]  Help: -h\n [-] e.g ./scanner.py -h\n")
    if len(sys.argv) <= 6:
        if sys.argv.__contains__("-s"):
            multihost_flag = 0
            ip_addr = sys.argv[1]
            port_start = sys.argv[2]
            port_end = sys.argv[3]
            beginScan(ip_addr,port_start,port_end,multihost_flag)
        elif sys.argv.__contains__("-m"):
            multihost_flag = 1
            ip_addr = sys.argv[1]
            port_start = sys.argv[2]
            port_end = sys.argv[3]
            beginScan(ip_addr,port_start,port_end,multihost_flag)
        else:
            clear()
            print(f"[+] Usage example: ./scanner.py <ip> <port_start> <port_end> \n[+] Use tag -h for more information.\n")
        #print(f" [+] DEBUG SCANNING {ip_addr} FROM {int(port_start)} TO {int(port_end)}")