import socket # Import socket module

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8080 # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Create a socket object
    s.connect((HOST, PORT)) # Connect to server
    s.sendall(b"Hello, world") # Send data to server
    data = s.recv(1024) # Receive data from the server

print(f"Received {data!r}") # Print the received data
