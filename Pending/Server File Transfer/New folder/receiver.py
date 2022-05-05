import socket
s = socket.socket()
host = input(str("Enter Host Address of the sender:- "))
port = int(input("Enter Hosted Port:- "))
s.connect((host,port))
print("Connected...")

filename = input(str("Enter file name to save incoming file:- "))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print("File Received Successfully....")