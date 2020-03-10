from core.connection.conn import *

def send_2_client(socket, user_input):
    data_in_bytes = bytes(user_input, "utf-8")
    socket.send(data_in_bytes)


def run_command(socket):
    print("[+] Running user Command")
    command = input("[+] Enter command to run: ")

    send_2_client(socket, command)

