import socket
import sys
import time

# Create a UDP client socket. Note the use of SOCK_DGRAM for UDP packets
while True:   # Run forever
    msgFromClient       = input("Enter your message :") # Enter your message
    bytesToSend         = str.encode(msgFromClient) # Convert to bytes
    serverAddressPort   = ("127.0.0.1", 20001) # Server IP and port
    bufferSize          = 1024 # Buffer size


# Create a UDP socket at client side
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) # Create a UDP socket
# Send to server using created UDP socket 
    UDPClientSocket.sendto(bytesToSend, serverAddressPort) # Send to server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize) # Receive from server
    msg = "Message from Server :{}".format(msgFromServer[0].decode()) # Decode the message
    #time.sleep(5)

    print(msg) # Print the message



