import socket
import sys
import os

argv = sys.argv

server_ip = argv[1]
server_port = int(argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((server_ip, server_port))
server.listen(1)
while True:
    client, client_addr = server.accept()
    file = client.recv(4096)
    client.send("file name received...".encode())
    binary = client.recv(4096)
    print("Binary: ", binary.decode())
    if binary.decode() == 'True':
        binary = True
    else :
        binary = False
    print("Requested file: ", file.decode())
    if file.decode() in os.listdir():
        chunk_size = 65536
        if binary : 
            f = open(file.decode() , 'rb')
        else :
            f = open(file.decode() , 'r')
        print("Sending file!")
        chunk = f.read(chunk_size)

        while chunk:
            if binary:
                client.send(chunk)
            else :
                client.send(chunk.encode())
            chunk = f.read(chunk_size)
        f.close()
        print("Done!")
    else :
        print("File not found!")
    client.close()
    break

server.close()