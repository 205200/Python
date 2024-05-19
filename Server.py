import socket

# Define the server's hostname or IP address and port
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port and listen for incoming connections
s.bind((HOST, PORT))
s.listen()

# Print messages indicating that the server is bound to the port and listening for connections
print("Socket binded to %s" % PORT)
print("Socket is listening....")

# Accept incoming connections and handle them
while True:
    # Accept a connection from a client
    con, addr = s.accept()
    print('Got connection from', addr)

    # Send a thank you message to the client
    con.send(b"Thank you for connecting... sent by server")

    # Receive data from the client
    data = con.recv(1024)
    print(f"Received {data!r}")

    # Close the connection with the client
    con.close()

    # Break the loop after handling one connection
    break
