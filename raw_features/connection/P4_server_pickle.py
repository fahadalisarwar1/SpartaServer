import socket
import pickle


HEADER_SIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ("", 8080)
s.bind(address)
print("[+] Waiting for incoming connection")
s.listen(5)
while True:
    client_socket, client_address = s.accept()
    print(f"[+] got a connection from {client_address}")

    d = {1: "Hey Ther", 2: "Listen to me"}

    data = pickle.dumps(d)
    packet = f"{len(data):<{HEADER_SIZE}}"+data

    print(packet)
    client_socket.send(packet)