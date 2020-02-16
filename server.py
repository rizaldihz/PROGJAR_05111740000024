import sys
import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 10000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(1024)
        if data:
            str_terima = data.decode()
            print(f'{client_address} : {str_terima}')
        else:
           break
        if str_terima == '/ls':
            to_kirim = os.listdir()
            to_kirim = '\n'.join([str(x) for x in to_kirim])
            connection.sendall(to_kirim.encode())
            continue
        string_command = str_terima.split(' ', 1)
        if(string_command[0] == '/up'):
            data = connection.recv(4)
            file_size = int.from_bytes(data,byteorder='big')
            current_size = 0
            file_name = string_command[1]
            with open(file_name+'_rec', 'wb+') as file_to_write:
                while current_size < file_size:
                    data = connection.recv(1024)
                    if not data:
                        break
                    file_to_write.write(data)
                    current_size = current_size + len(data)
            file_to_write.close()
            msg = 'Sukses mengupload '+string_command[1]
            connection.sendall(msg.encode())
            continue

        if string_command[0] == '/get':
            file_kirim = string_command[1]
            size_file = os.path.getsize(file_kirim)
            connection.send(size_file.to_bytes(4,byteorder='big'))
            print(f"uploading {file_kirim}")
            with open(file_kirim, 'rb') as file_to_send:
                for data in file_to_send:
                    connection.sendall(data)
            file_to_send.close()
            msg = 'Sukses mendownload ' + string_command[1]
            connection.sendall(msg.encode())
            continue

        connection.sendall(data)


    connection.close()
