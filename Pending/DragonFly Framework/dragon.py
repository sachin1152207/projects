#coding=utf-8
#This Framework is Devloped by:~ Badhshah Hacker
#Coded by:- Sachin Shrivastv
#This framework is Open Source
#Reseverd 2020

import os,sys,time


def start():
	titik = ["/",'''\ ''',"/",'''\ ''',"/",'''\ ''',"/",'''\ ''',"/",'''\ ''',"/",'''\ ''',"/",'''\ ''',"/",'''\ ''',"/",'''\ ''',"/",'''\ ''']
	for o in titik:
		print("\r  \033[1;97mStarting..............\033[1;93m"+o),;sys.stdout.flush();time.sleep(0.2)
start()
time.sleep(2)
os.system('clear')

def banner():
	print("                         ,     \    /      ,")
	print("""                      / \    )\__/(     / \ """)
	print("""                     /   \  (_\  /_)   /   \   """)
	print('   <__________________/_____\__\@  @/___/_____\_________________>')
	print('    |                          |\../|                          |')
	print('    |                           \VV/                           |')
	print('    |                   \033[1;93mOwner:~  Badhshah\033[1;97m                      |')	
	print('    |                 \033[1;93mAuthor:~   Sachin Shrivastv\033[1;97m              |')
	print('    |                 \033[1;93mYoutube:~  Badhshah Hacker\033[1;97m               |')	
	print('    |__________________________________________________________|')
	print('''                |    /\ /      \\\        \ /\    |''')
	print('                  |  /   V        ))        V   \  |')
	print('                  |/             //               \|')
	print('''                `              V                 `''')

def main():
	os.system('clear')
	banner()
	select()
def fb_tool():
	print("1....... Brutefroce")
	print("2....... FB Bot")
	print("3....... FB Login Bot")
	print("4....... Token Generator")
def net_tool():
	print("1....... DDos-Attack")
	print("2....... Port Scanner")
	print("3....... IP-Lookup")
	print("4....... Header Checker")
	print("5....... Reverse Lookup")
def select():
	sel = raw_input('@dragonFly:~ ').lower()
	if sel =='':
		print('Check Your Command...')
		time.sleep(1)
		main()
	elif sel =='help':
		print('''\033[1;93mCommands:\033[1;97m
	run                  :          Run tool (Eg: run A-Rat)
	clear                :          Clear Terminal Screen 
	restart              :          Restart DragonFly Framework
	banner				 :          Print Banner 
	show tool            :          Show all tools
	show modules         :          Show specific tool (Eg: show_module facebook)''')
		select()
	elif sel =='clear':
		os.system('clear')
		select()
	elif sel =='restart':
		os.system('python2 dragon.py')
	elif sel =='show tools' or 'show-tools':
		print("fb_tool")
		print("net_tool")
		select()
	elif sel =='banner':
		main()
	elif sel =='show_module facebook':
		fb_tool()
		select()
	elif sel =='show_module network':
		net_tool()
		select()
	else:
		print("Check Your Command.....")
	
		 
if __name__ == '__main__':
	main()
		
