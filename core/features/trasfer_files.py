def upload_files(my_socket):
    print("[+] Uploading files to client")
    with open("wallpaper.jpeg") as file:
        data = file.read()
        my_socket.send_data_bytes(data)