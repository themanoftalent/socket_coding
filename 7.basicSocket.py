#here we create a simple socket 

import socket # for socket
import sys

# create a socket object
def socket_connect(host):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" %(err))

socket_connect("www.google.com")
