import socket
s = socket.socket()
host = "127.0.0.1"
port = 4546
s.bind((host,port))
s.listen(1)
print(host)
print("Waiting for any connection...")
conn, addr = s.accept()
print(addr, "Has been connected to the server")

filename = input(str("Enter file name here:- "))
file = open(filename, 'rb')
file_data = file.read(104857600)
conn.send(file_data)
print("File sent successfully....")
