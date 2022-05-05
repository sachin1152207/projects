#utf-8
#2021 All Right Reseverd
#The Coding Credits Goes To Our Respected
#Devloper Sachin Shrivastv
import socket,sys,time,os
os.system('clear') #Change it
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def typing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)
def local_server():
	ip = "127.0.0.1"
	banner2()
	port = int(input('Enter Your Local Hosted Port:~ '))
	try:
		s.connect((ip,port))
		typing('Server Has Accept The Request Of Client')
		time.sleep(1)
		os.system('clear')
		banner2()
		while 1:
			recv_msg = s.recv(1024)
			recv_msg = recv_msg.decode()
			print(recv_msg)
			msg = input("Enter Your Message:- ")
			msg = client_id +':~ ' + msg
			msg = msg.encode()
			s.send(msg)
	except (ConnectionRefusedError):
		print("Failed To Connect With Server!! Please Activate The Server Frist...")
		time.sleep(1)
		os.system('exit')
def public_server():
	banner2()
	public_ip = input("Enter Your Public Hosted IP:~ ")
	port = int(input("Enter Your Public Hosted Port:~ "))
	ip = public_ip
	try:
		s.connect((ip,port))
		typing('Server Has Accept The Request Of Client')
		time.sleep(1)
		os.system('clear')
		banner2()
		while 1:
			recv_msg = s.recv(1024)
			recv_msg = recv_msg.decode()
			print(recv_msg)
			msg = input("Enter Your Message:- ")
			msg = client_id +':~ ' + msg
			msg = msg.encode()
			s.send(msg)
	except (ConnectionRefusedError):
		print("Failed To Connect With Server!! Please Activate The Server Frist...")
		time.sleep(1)
		os.system('exit')
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
def banner2():
	print("                         ,     \    /      ,")
	print("""                        / \    )\__/(     / \ """)
	print("""                       /   \  (_\  /_)   /   \   """)
	print('   <__________________/_____\__\@  @/___/_____\_________________>')
	print('    |                          |\../|                          |')
	print('    |                           \VV/                           |')
	print("    |                         "+client_id+"                         |")
	print('    |                     Owner:~  Badhshah                    |')	
	print('    |                   Author:~   Sachin Shrivastv            |')
	print('    |                 Coder:~  Mr. Piece & C07 Ghost           |')	
	print('    |__________________________________________________________|')
	print('''                |    /\ /      \\\        \ /\    |''')
	print('                |  /   V        ))        V   \  |')
	print('                |/             //               \|')
	print('''                `              V                 `''')
banner()
client_id = input("Enter Your 8 Digit Client ID:~ ")
if len(client_id) >8 or len(client_id) <8:
	typing("Sorry, we accept only 8 digit client id")
	time.sleep(0.5)
else:
	time.sleep(0.5)
	os.system('clear') #Change it
	banner2()
	print("1~~~~~>> Local Host")
	print("2~~~~~>> Public Host")
	ch = input("Select Your Host Option:~ ")
	if ch=="":
		typing('Something went wrong!!')
		time.sleep(1)
		os.system('exit')
	elif ch=="1":
		os.system('clear')
		local_server()
		time.sleep(1)
	elif ch=="2":
		os.system('clear')
		public_server()
		time.sleep(1)
	else:
		typing('Something went wrong!!')
		time.sleep(1)
		os.system('exit')
		
	
