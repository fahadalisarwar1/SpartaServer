




def run_command(my_socket):
    print("[+] Running user Command")
    keep_running = True
    print("[+] Enter Command ")
    while keep_running:
        command = input(">> ")
        my_socket.send_data(command)
        if command == "stop" or command == "exit":
            keep_running = False

        my_socket.receive_command_result()

