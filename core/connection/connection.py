import socket
import pickle
import os

HEADERSIZE = 10

CHUNK_SIZE = 4 * 1024

END_DELIMETER = "*END_OF_FILE*"

COMMAND_END = "<END_OF_COMMAND>"

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

    def receive_file(self):
        print("[+] Receiving File")

    def receive_command_result(self):
        print("[+] Receiving Command result")
        full_result = b''
        while True:
            chunk = self.connection.recv(CHUNK_SIZE)
            if chunk.endswith(COMMAND_END.encode()):
                chunk += chunk[:-len(COMMAND_END)]
                full_result += chunk
                break
            full_result += chunk

        print(full_result.decode())

    def Close(self):
        self.socket.close()
