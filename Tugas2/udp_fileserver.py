import socket


SERVER_IP = '127.0.0.1'
SERVER_PORT = 5006
NAMAFILE='coba.png'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

fp = open(NAMAFILE,'wb+')
ditulis=0

counter=0
while counter < 6767:
    data, addr = sock.recvfrom(1024)
    counter=counter+len(data)
    print(addr," blok ", counter,"panjang : ",len(data), data)
    fp.write(data)


fp.close()
