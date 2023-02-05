import socket
import os, sys

argv = sys.argv
print(argv)
server_ip = argv[1]
server_port = int(argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip, server_port))

file = None
binary = False
if argv[3] == '-b':
    binary = True
    file = argv[4]
else :
    file = argv[3]

f = None
if binary:
    f = open('ftp_'+file, 'bw')
else :
    f = open('ftp_'+file, 'w')

client.send(file.encode())
reply = client.recv(4096)
if binary:
    client.send('True'.encode())
else :
    client.send("False".encode())

print("File requested: ", file)
data = 'None'
print("Starting Transfer!")
while data:
    data = client.recv(65536)
    if binary:
        f.write(data)
    else :
        f.write(data.decode())
f.close()
print("File Transfer complete!")
client.close()