import socket


def Create_connection(ip="", port = 8080, backlog = 5):

    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    skt.bind((ip, port))
    skt.listen(backlog)
    return skt

def Accept_connection(skt):
    return skt.accept()

def send_data(skt, data):
    data_in_bytes = bytes(data, "utf-8")
    skt.send(data_in_bytes)

def receive_data(skt):
    data_in_bytes = skt.recv(1024)
    data = data_in_bytes.decode('utf-8')
    return data

def close(skt):
    skt.close()
