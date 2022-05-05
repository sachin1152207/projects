#utf-8
#2021 All Right Reseverd
#The Coding Credits Goes To Our Respected
#Devloper Sachin Shrivastv
import socket,sys,time,os
os.system('cls') #Change it
def typing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)
def banner():
	print("                         ,     \    /      ,")
	print("""                        / \    )\__/(     / \ """)
	print("""                       /   \  (_\  /_)   /   \   """)
	print('   <__________________/_____\__\@  @/___/_____\_________________>')
	print('    |                          |\../|                          |')
	print('    |                           \VV/                           |')
	print('    |                        Server Chat                       |')
	print('    |                     Owner:~  Badhshah                    |')	
	print('    |                   Author:~   Sachin Shrivastv            |')
	print('    |                 Coder:~  Mr. Piece & C07 Ghost           |')	
	print('    |__________________________________________________________|')
	print('''                |    /\ /      \\\        \ /\    |''')
	print('                |  /   V        ))        V   \  |')
	print('                |/             //               \|')
	print('''                `              V                 `''')
def server_local():
	port = int(input("Enter Your Unreversed Local Port:~ "))
	time.sleep(0.5)
	typing("The Server Has Been Hosted Sucessfully on Local Network")
	time.sleep(0.5)
	typing("Waiting for the client response....")
	s.bind((ip,port))
	s.listen(1)
	conn,addr = s.accept()
	time.sleep(0.5)
	os.system('cls')
	banner()
	typing("All The Client Has Been Connected To The Server on Local Network")
	time.sleep(1)
	os.system('cls')
	banner()
	while 1:
		msg = input("Enter Your Message:~ ")
		msg = "Server:~ " + msg
		msg = msg.encode()
		conn.send(msg)
		recv_msg = conn.recv(1024)
		recv_msg = recv_msg.decode()
		print(recv_msg)
	
def server_public():
	port = int(input("Enter Your Unreversed Hosted Port:~ "))
	time.sleep(0.5)
	typing("The Server Has Been Hosted Sucessfully on Public Network")
	time.sleep(0.5)
	typing("Waiting for the client response....")
	s.bind((ip,port))
	s.listen(1)
	conn,addr = s.accept()
	time.sleep(0.5)
	os.system('cls')
	banner()
	typing("All The Client Has Been Connected To The Server on Public Network")
	time.sleep(1)
	os.system('cls')
	banner()
	while 1:
		msg = input("Enter Your Message:~ ")
		msg = "Server:~ " + msg
		msg = msg.encode()
		conn.send(msg)
		recv_msg = conn.recv(1024)
		recv_msg = recv_msg.decode()
		print(recv_msg)
	
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
banner()
print("1~~~~~>> Local Host")
print("2~~~~~>> Public Host")
ch = input("Select Your Host Option:~ ")
if ch =="":
	print("Something went wrong!!")
	time.sleep(0.5)
	os.system('exit')
elif ch =="1": #Local Port
	os.system('cls') #Change it
	banner()
	server_local()
elif ch=="2": #Public Port
	os.system('cls') #Change it
	banner()
	server_public()
else:
	print("Something went wrong!!")
	time.sleep(0.5)
	os.system('exit')