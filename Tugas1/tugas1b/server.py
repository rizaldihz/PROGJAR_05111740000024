import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
host = input('host: ')
port = int(input('port: '))
server_address = (host, port)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")

    data = connection.recv(64)
    file_name = data.decode()
    print(file_name)
    if os.path.exists(file_name):
        connection.sendall('ok'.encode())
        with open(file_name, 'rb') as file_to_send:
            for byte in file_to_send:
                connection.sendall(byte)
        file_to_send.close()
        msg = 'Sukses mendownload '+file_name
        connection.sendall(msg.encode())
    else:
        print('file not found')
        msg = 'file not found'
        connection.sendall(msg.encode())
    connection.close()
