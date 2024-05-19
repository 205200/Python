import socket

# Define the server's hostname or IP address and port
HOST = "127.0.0.1"
PORT = 65432

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server
s.connect((HOST, PORT))

# Send a message to the server
s.send(b"Hello, world.... sent by client")

# Receive data from the server
data = s.recv(1024)

# Print the received data
print(f"Received {data!r}")

# Close the socket connection
s.close()
