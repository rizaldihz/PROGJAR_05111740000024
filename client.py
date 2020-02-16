import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print(f"connecting to {server_address}")
sock.connect(server_address)


try:
    while True:
        # Send data
        message = input()
        print(f"sending : {message}")
        temp = message
        temp = temp.split(' ',1)
        sock.sendall(message.encode())
        flag = 0
        if temp[0] == '/up':
            file_kirim = temp[1]
            size_file = os.path.getsize(file_kirim)
            sock.send(size_file.to_bytes(4,byteorder='big'))
            print(f"uploading {file_kirim}")
            with open(file_kirim, 'rb') as file_to_send:
                for data in file_to_send:
                    sock.sendall(data)
            file_to_send.close()

        if (temp[0] == '/get'):
            data = sock.recv(4)
            file_size = int.from_bytes(data, byteorder='big')
            current_size = 0
            file_name = temp[1]
            with open(file_name + '_get', 'wb+') as file_to_write:
                while current_size < file_size:
                    data = sock.recv(1024)
                    if not data:
                        break
                    if len(data) + current_size > file_size:
                        data = data[:file_size - current_size]  # trim additional data
                        data_dump = data[(file_size - current_size) : current_size]
                        flag = 1
                    file_to_write.write(data)
                    current_size = current_size + len(data)
            file_to_write.close()

        # Look for the response
        if flag == 1 : data = data_dump
        else : data = sock.recv(1024)
        print(f"recieved : {data.decode()}")
finally:
    print("closing")
    sock.close()
