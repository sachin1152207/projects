import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
	clientsocket, address = s.accept()
	print("Connection from",address,"has been establisted!")
	clientsocket.send(bytes("Hello, This Is the Test Of Socket Module Packets Streaming Methods", "utf-8"))
	clientsocket.close()