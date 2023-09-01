import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 4000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for a connection...")

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

while True:
    # Receive a message from the client
    client_message = client_socket.recv(1024).decode('utf-8')
    if not client_message:
        break
    
    print(f"Client: {client_message}")
    
    # Send a response back to the client
    server_message = input("Server: ")
    client_socket.send(server_message.encode('utf-8'))

# Close the sockets
client_socket.close()
server_socket.close()
