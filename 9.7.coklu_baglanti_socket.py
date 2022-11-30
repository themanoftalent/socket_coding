# multi connection socket server with select

import socket
import select
import sys

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

# create a list of sockets for select
inputs = [serversocket]

while True:
    # get the list sockets which are ready to be read through select
    # 4th arg, time_out  = 0 : poll and never block
    read_sockets, write_sockets, error_sockets = select.select(inputs, [], [])

    for sock in read_sockets:
        # new connection
        if sock == serversocket:
            # handle the case in which there is a new connection recieved through serversocket
            sockfd, addr = serversocket.accept()
            inputs.append(sockfd)
            print ("Client (%s, %s) connected" % addr)

        # some incoming message from a client
        else:
            # data recieved from client, process it
            try:
                # receiving data from the socket.
                data = sock.recv(1024)
                if data:
                    # there is something in the socket
                    print (data)
                    sock.send("OK ... " + data)
                else:
                    # remove the socket that's broken    
                    if sock in inputs:
                        inputs.remove(sock)
                    # at this stage, no data means probably the connection has been broken
                    sock.close()

            # exception 
            except:
                continue

serversocket.close()
