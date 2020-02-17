import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
host = input('host: ')
port = int(input('port: '))
server_address = (host, port)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    file_name = input('to download: ')
    sock.sendall(file_name.encode())
    data = sock.recv(1024)
    if data.decode() == 'ok':
        with open(file_name+'_get', 'wb+') as file_to_write:
            data = sock.recv(1024)
            while data:
                file_to_write.write(data)
                data = sock.recv(1024)
        file_to_write.close()
        data = sock.recv(1024)
        print(f'{data.decode()}')
    else:
        print(f'{data.decode()}')
finally:
    print("closing")
    sock.close()
