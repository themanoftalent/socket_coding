
import socket # for socket
import sys

# get a message from scoket
def get_message(sock): # get a message from socket
    message = '' # initialize message 
    while True:
        chunk = sock.recv(4096) # get a chunk of data from socket 
        if chunk == '': # if chunk is empty, break
            raise RuntimeError("socket connection broken") # raise an exception
        message += chunk # add chunk to message 
        if message.endswith('\r \r '): # if message ends with '\r
            break # break
    return message # return message
s= input("Enter the host message: ") # get a host name from user
print(s) # print host name
