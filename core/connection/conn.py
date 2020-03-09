import socket


class Connection:
    def __init__(self, ip, port):
        self.skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.skt.bind((ip, port))

    def Listen(self, backlog=5):
        self.skt.listen(backlog)

    def Accept(self):
        return self.skt.accept()

    