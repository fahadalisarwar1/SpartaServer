import socket

if __name__ == "__main__":
    local_ip = ""
    local_port = 8080
    address = (local_ip, local_port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(address)

    s.listen(5)

    while True:
        print("[+] Listening for incoming connections")
        client_socket, client_address = s.accept()
        print("[+] connected with : ", client_address)
        msg2send = bytes("welcome to server", encoding="utf-8")
        client_socket.send(msg2send)

