import socket
import pickle

HEADERSIZE = 10

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


    def Close(self):
        self.socket.close()