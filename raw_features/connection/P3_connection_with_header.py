import socket

HEADER_SIZE = 10

if __name__ == "__main__":
    local_ip = ""
    local_port = 8081
    address = (local_ip, local_port)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(address)

    s.listen(5)
    while True:
        print("[+] Listening for incoming connections")
        client_socket, client_address = s.accept()
        print("[+] connected with : ", client_address)

        msg = "This is the message i want to send"
        msg = f'{len(msg):<{HEADER_SIZE}}' + msg



        msg2send = bytes(msg, encoding="utf-8")
        client_socket.send(msg2send)
        client_socket.close()




