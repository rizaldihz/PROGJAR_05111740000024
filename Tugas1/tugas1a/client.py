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
    file_kirim = input('to upload: ')
    if os.path.exists(file_kirim):
        sock.sendall(file_kirim.encode())
        print(f"uploading {file_kirim}")
        with open(file_kirim, 'rb') as file_to_send:
            for byte in file_to_send:
                sock.sendall(byte)
        file_to_send.close()
    else:
        print('file not found')
finally:
    print("closing")
    sock.close()
