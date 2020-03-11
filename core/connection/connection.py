import socket
import pickle
import os

HEADERSIZE = 10

CHUNK_SIZE = 4 * 1024

END_DELIMETER = "*END_OF_FILE*"

class ServerConnection:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def CreateConnection(self, ip="", port=8080):
        self.socket.bind((ip, port))
        self.ip=ip
        self.port=port

    def ListenIncoming(self, backlog=5):
        self.socket.listen(backlog)

    def AcceptConnection(self):
        self.connection, self.client_address = self.socket.accept()

        return  (self.connection, self.client_address)

    def send_data(self,  user_input):
        self.data_in_bytes = bytes(user_input, "utf-8")
        self.connection.send(self.data_in_bytes)

    def receive_data(self):
        self.data_in_bytes = self.connection.recv(1024)
        self.data = self.data_in_bytes.decode('utf-8')
        return self.data

    def send_data_bytes(self, data):
        print("[+] Sending data as bytes")
        self.connection.send(data)

    def receive_serilized(self):
        print("[+] Receiving serialized data")
        full_msg = b''
        new_msg = True
        full_recvd = True
        while full_recvd:
            msg = self.connection.recv(1024)
            if new_msg:
                msglen = int(msg[:HEADERSIZE])
                new_msg = False


            full_msg += msg

            if len(full_msg) - HEADERSIZE == msglen:

                self.cmd_dict = (pickle.loads(full_msg[HEADERSIZE:]))
                new_msg = True
                full_msg = b""
                full_recvd = False

        return self.cmd_dict

    def send_files(self, filename):
        print("[+] Sending File : ", filename)

        self.send_data(filename)

        if os.path.exists(filename):
            print("[+] File exists!")
            with open(filename, "rb") as file:
                chunk = file.read(CHUNK_SIZE)

                while len(chunk) > 0:
                    self.connection.send(chunk)
                    chunk = file.read(CHUNK_SIZE)
                self.connection.send(END_DELIMETER.encode())

        else:
            self.connection.send("NOT_FOUND".encode())
            print("[-] File doesn't exist!")


    def Close(self):
        self.socket.close()
