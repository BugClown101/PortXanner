#!/usr/bin/python3


print( "-" * 70)
print("PortXanner")
print( "-" * 70)
import socket
import time
start_time = time.time()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))

print( "-" * 70)

print("Scanning Under Process",)

print( "-" * 70)

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is CLOSED")
    else:
        print("The port is OPEN")

portScanner(port)

end_time = time.time()
print("Time elapsed :",end_time - start_time)