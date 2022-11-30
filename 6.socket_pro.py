# An example script to connect to Google using socket
# programming in Python
import socket # for socket
import sys

def socket_connect(host):
    try:
        global sock
        sock = socket.socket()
        print ("Socket successfully created")
    except socket.error as err:
        print ("socket creation failed with error %s" %(err))

    # default port for socket
    port = 80

    try:
        host_ip = socket.gethostbyname(host)
    except socket.gaierror:

        # this means could not resolve the host
        print ("there was an error resolving the host")
        sys.exit()

    # connecting to the server
    sock.connect((host_ip, port))

    print ("the socket has successfully connected to google  on port == %s" %(host_ip))

if __name__ == "__main__":
    socket_connect("www.google.com")


