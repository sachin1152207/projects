#Coding=utf-8
#This Script is Written By:- Sachin Shrivastv
#This Script Open Source
#Devloper Allow to Edit & debug this Script.
#Location:- Nepal
import os,time,sys
#Bannering Start#
logO='                    ------------------------------  '
logo='                  |   \033[1;93m_____         _______        \033[1;97m| '
logo1='                  |  \033[1;93m/ ____|       |__   __|       \033[1;97m| '  
logo2='                  |  \033[1;93m| (__     __ _   | |  __   __ \033[1;97m| '
logo3='                  |  \033[1;93m\___ \   / _` |  | |  \ \ / / \033[1;97m| '
logo4='                  |  \033[1;93m____) | | (_| |  | |   \ V /  \033[1;97m| '
logo5='                  | \033[1;93m|_____/   \__,_|  |_|    \_/   \033[1;97m| '
logo6='                  |________________________________| '
logo7=('        }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{')
logo8=('}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{')
#Bannering Close#
def bannering():
	print(logO)
	time.sleep(0.1)
	print(logo)
	time.sleep(0.1)
	print(logo1)
	time.sleep(0.1)
	print(logo2)
	time.sleep(0.1)
	print(logo3)
	time.sleep(0.1)
	print(logo4)
	time.sleep(0.1)
	print(logo5)
	time.sleep(0.1)
	print(logo6)
	time.sleep(0.1)
	print(logo7)
	time.sleep(0.1)
	print(logo8)
def install():
	os.system('clear')
	os.system('apt update')
	os.system('clear')
	print('\n\nInstalling...[ 1% ] [\033[1;91m#....................\033[1;97m]\n\n') 
	os.system('apt upgrade')
	os.system('clear')
	print('\n\nInstalling...[ 1% ] [\033[1;91m##...................\033[1;97m]\n\n')
	os.system('pkg install python')
	os.system('clear')
	print('\n\nInstalling...[ 7% ] [\033[1;91m#####................\033[1;97m]\n\n')
	os.system('pkg install python2')
	os.system('clear')
	print('\n\nInstalling...[ 9% ] [\033[1;91m#######..............\033[1;97m]\n\n')
	os.system('pkg install python3')
	os.system('clear')
	print('\n\nInstalling...[ 16% ] [\033[1;91m########.............\033[1;97m]\n\n')
	os.system('pkg install figlet')
	os.system('clear')
	print('\n\nInstalling...[ 29% ] [\033[1;91m########............\033[1;97m]\n\n')
	os.system('pkg install git')
	os.system('clear')
	print('\n\nInstalling...[ 38% ] [\033[1;91m########............\033[1;97m]\n\n')
	os.system('pkg install php')
	os.system('clear')
	print('\n\nInstalling...[ 47% ] [\033[1;91m#########...........\033[1;97m]\n\n')
	os.system('pkg install uncompyle6')
	os.system('clear')
	print('\n\nInstalling...[ 59% ] [\033[1;91m##########..........\033[1;97m]\n\n')
	os.system('pkg install unzip')
	os.system('clear')
	print('\n\nInstalling...[ 67% ] [\033[1;91m##########..........\033[1;97m]\n\n')
	os.system('pkg install tsu')
	os.system('clear')
	print('\n\nInstalling...[ 72% ] [\033[1;91m##########..........\033[1;97m]\n\n')
	os.system('pkg install termux-api')
	os.system('clear')
	print('\n\nInstalling...[ 79% ] [\033[1;91m###########.........\033[1;97m]\n\n')
	os.system('pkg install nmap')
	os.system('clear')
	print('\n\nInstalling...[ 81% ] [\033[1;91m###########.........\033[1;97m]\n\n')
	os.system('pkg install perl')
	os.system('clear')
	print('\n\nInstalling...[ 84% ] [\033[1;91m###########.........\033[1;97m]\n\n')
	os.system('pkg install openssl')
	os.system('clear')
	print('\n\nInstalling...[ 88% ] [\033[1;91m############........\033[1;97m]\n\n')
	os.system('pkg install openssh')
	os.system('clear')
	print('\n\nInstalling...[ 93% ] [\033[1;91m##############......\033[1;97m]\n\n')
	os.system('pkg install nano')
	os.system('clear')
	print('\n\nInstalling...[ 95% ] [\033[1;91m##################..\033[1;97m]\n\n')
	os.system('pip install mechanize')
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip2 install mechanize')
	os.system('pip2 install requests')
	os.system('pip2 install colorama')
	os.system('pip3 install requests')
	os.system('pip3 install mechanize')
	os.system('pip3 install requests')
	os.system('pip3 install colomara')
	os.system('clear')
	print('\n\nInstalling...[ 100% ] [\033[1;91m###################\033[1;97m]\n\n')
	time.sleep(1)
	main()

def main():
	os.system('clear')
	bannering()
	print('\033[1;93m{1}~~~>>  Show Tools')
	print('{2}~~~>>  Show Tools Categories')
	print('{3}~~~>>  Update SaTv')
	print('{0}~~~>>  Exit')
	sel = raw_input('\033[1;97mSelect Option:~ ')
	if sel =='':
		print('\033[1;91mWrong Input')
		time.sleep(1)
		os.system('clear')
		main()
	elif sel =='1':
		tool()
	elif sel =='2':
		typetool()
	elif sel =='3':
		os.system('cd -')
		os.system('rm -rf SaTv')
		os.system('git clone https://www.github.com/Sac56/SaTv')
		os.system('cd SaTv')
		print('SaTv Updated Sucessful')
		time.sleep(1)
		os.system('clear')
		main()
	elif sel =='0':
		print('Exit')
		os.system('exit')
	else:
		print('\033[1;91mWrong Input')
		time.sleep(1)
		os.system('clear')
		main()
def typetool():
	os.system('clear')
	bannering()
	print('{1} Infromation Gathering')
	print('{2} Vulnerability Scanner')
	print('{3} Exploitation Tools')
	print('{4} Wireless Testing')
	print('{5} Forencics Tools')
if __name__ == '__main__':
	install()

	
