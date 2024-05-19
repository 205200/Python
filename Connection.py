import socket  # Import the socket module
import sys  # Import the sys module for system-specific parameters and functions

try:
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")
except socket.error as err:
    # Handle socket creation failure
    print("Socket creation failed with error %s" % (err))

# Default port for HTTP connections
port = 80

try:
    # Get the IP address of the host (www.google.com)
    host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    # Handle hostname resolution failure
    print("There was an error resolving the host")
    sys.exit()

# Connect to the server (Google) using its IP address and port
s.connect((host_ip, port))

# Print connection success message and the IP address of Google
print("The socket has successfully connected to Google")
print(host_ip)
