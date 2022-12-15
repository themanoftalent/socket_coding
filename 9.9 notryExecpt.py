import socket  # for socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

# default port for socket
port = 80
host_ip = socket.gethostbyname('www.google.com')

# this means could not resolve the host
print("there was an error resolving the host")
sys.exit()

# connecting to the server
s.connect((host_ip, port))
print("the socket has successfully connected to google")
