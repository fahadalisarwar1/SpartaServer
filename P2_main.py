from core.connection.connection import *
from core.connection.handler import *

if __name__== "__main__":
    my_socket = ServerConnection()
    my_socket.CreateConnection("", 8080)
    print("[+] Waiting for incoming connection")

    my_socket.ListenIncoming()

    my_Conn, _ = my_socket.AcceptConnection()

    handleConnection(my_socket)
    my_socket.Close()
