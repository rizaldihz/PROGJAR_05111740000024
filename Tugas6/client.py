import socket
import os
import json

TARGET_IP = "127.0.0.1"
TARGET_PORT = 10001


class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP,TARGET_PORT)
        self.sock.connect(self.server_address)
    def proses(self,cmdline):
        try:
            return self.sendstring(cmdline)
        except IndexError:
                return "-Maaf, command tidak benar"
    def sendstring(self,string):
        try:
            self.sock.sendall(string.encode())
            receivemsg = ""
            while True:
                data = self.sock.recv(64)
                if (data):
                    receivemsg = "{}{}" . format(receivemsg,data.decode())
                    if receivemsg[-2:]=='\r\n':
                        return receivemsg
        except:
            self.sock.close()
            return { 'status' : 'ERROR', 'message' : 'Gagal'}


if __name__=="__main__":
    cc = ChatClient()
    while True:
        cmdline = input("Command:")
        cmdline += '\r\n'
        print(cc.proses(cmdline))

