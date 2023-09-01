import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 4000)
client_socket.connect(server_address)

while True:
    # Send a message to the server
    client_message = input("Client: ")
    client_socket.send(client_message.encode('utf-8'))
    
    # Receive a response from the server
    server_message = client_socket.recv(1024).decode('utf-8')
    print(f"Server: {server_message}")

# Close the socket
client_socket.close()
