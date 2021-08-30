#!/bin/python3
import sys
import socket
from datetime import datetime
#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started:"+str(datetime.now()))
print("-" * 50)


try:
    for port in range(1,65535): #Example for "port in range(50,81)"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #to connect to a port , if the port not connectable
        result = s.socket_ex((target,port)) #returns as error indicator
        #print("Checking port {}".format(port)) #here is checking all ports (also include the open ports)
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt: #KeyboardInterrupt is a User Signal which is executed by User
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:  #It means that your given host name ' ' is invalid
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error: #A "socket error" indicates that data sent over the network has not arrived in time
    print("Couldn't connect to server.")
    sys.exit()

#python3 scanner.py <ip>



























