

def become_persistant(my_socket):
    print("[+] Becoming persistant")
    res = my_socket.receive_data()
    print(res)