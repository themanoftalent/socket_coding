# An example script to connect to Google using socket
# programming in Python

import socket # for socket
import sys

def socket_connect(host): # create an INET, STREAMing socket 
    try:
        global sock # global variable to use socket outside function
        sock = socket.socket() # default values are used for arguments
        print ("Socket successfully created") # socket created
    except socket.error as err: # if socket creation fails print error
        print ("socket creation failed with error %s" %(err))

    # default port for socket
    port = 80 # port for socket

    try:
        host_ip = socket.gethostbyname(host) # get ip address of host 
    except socket.gaierror: # if host is not found print error

        # this means could not resolve the host
        print ("there was an error resolving the host") # error
        sys.exit()

    # connecting to the server
    sock.connect((host_ip, port)) # connect to host using port 

    print ("the socket has successfully connected to google  on port == %s" %(host_ip))

if __name__ == "__main__":
    socket_connect('www.google.com')
