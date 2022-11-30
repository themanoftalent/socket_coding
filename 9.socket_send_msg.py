
import socket # for socket
import sys

# send a message from scoket to server
def socket_send_message(host, message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Failed to create socket. Error code: " + str(msg[0]) + " , Error message : " + msg[1])
        sys.exit();

    print("Socket Created")

    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror: #Gaieerror is an exception raised when a getaddrinfo() call fails.
       
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    
    print("Ip address of " + host + " is " + remote_ip)

    #Connect to remote server
    s.connect((remote_ip, 80))

    print("Socket Connected to " + host + " on ip " + remote_ip)

    #Send some data to remote server
    #message = "GET / HTTP/1.1\r \r  \r " #GET / HTTP/1.1\r

    try:
        #Set the whole string
        s.sendall(message)
    except socket.error:
        #Send failed
        print("Send failed")
        sys.exit()

    print("Message send successfully")

    #Now receive data
    reply = s.recv(4096)
    return reply

socket_send_message("www.google.com", "GET / HTTP/1.1\r \r  \r ")




