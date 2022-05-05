#coding=utf-8
#This script is written by by Sachin Shrivastv
#Date:- 2020/08/02
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf-8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def exit():
	print "\033[1;98mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def printing (z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r \033[1;97mPlease Wait \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

logo='\033[1;92m▐         \033[1;97m###            ###     \033[1;91m*********       *********     \033[1;97mPPPPPPPPPPPPPP       \033[1;92m▐'
logo2='\033[1;92m▐         \033[1;97m## #          # ##    \033[1;91m************   ************    \033[1;97mPP             P     \033[1;92m▐'
logo3='\033[1;92m▐         \033[1;97m##  #        #  ##   \033[1;91m************** **************   \033[1;97mPP              P    \033[1;92m▐'
logo4='\033[1;92m▐         \033[1;97m##   #      #   ##   \033[1;91m*****************************   \033[1;97mPP              P    \033[1;92m▐'
logo5='\033[1;92m▐         \033[1;97m##    #    #    ##   \033[1;91m*****************************   \033[1;97mPP             P     \033[1;92m▐'
logo6='\033[1;92m▐         \033[1;97m##     #  #     ##    \033[1;91m***************************    \033[1;97mPPPPPPPPPPPPPP       \033[1;92m▐'
logo7='\033[1;92m▐         \033[1;97m##      ##      ##      \033[1;91m************************     \033[1;97mPP                   \033[1;92m▐'
logo8='\033[1;92m▐         \033[1;97m##	          ##        \033[1;91m********************       \033[1;97mPP                   \033[1;92m▐'
logo9='\033[1;92m▐         \033[1;97m##	          ##          \033[1;91m****************         \033[1;97mPP                   \033[1;92m▐'
logo10='\033[1;92m▐         \033[1;97m##	          ##            \033[1;91m************           \033[1;97mPP                   \033[1;92m▐'
logo11='\033[1;92m▐         \033[1;97m##	          ##              \033[1;91m********             \033[1;97mPP                   \033[1;92m▐'
logo12='\033[1;92m▐         \033[1;97m##	          ##                \033[1;91m***                \033[1;97mPP                   \033[1;92m▐'
logo13='\033[1;92m▐         \033[1;97m##	          ##                 \033[1;91m*                 \033[1;97mPP                   \033[1;92m▐'
logo14='\033[1;92m▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌'
logo15='\033[1;92m▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌'

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
def LOGO():
 
	print(logo14)
	print(logo)
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
	time.sleep(0.1)
	print(logo9)	
	time.sleep(0.1)
	print(logo10)
	time.sleep(0.1)	
	print(logo11)
	time.sleep(0.1)
	print(logo12)
	time.sleep(0.1)
	print(logo13)
	time.sleep(0.1)
	print(logo15)
	
def login():
	os.system('clear')
	LOGO()
	username = raw_input('Enter Username:~ ')
	if username =='':
		print('Wrong Username[!]')
		time.sleep(1)
		login()
	elif username =='BROKENHEART' or username =='brokenheart':
		password = raw_input('Enter Password:~ ')
		if password =='':
			print('Wrong Password[!]')
			time.sleep(1)
			login()
		elif password =='M-LOVE-P' or password =='m-love-p':
			printing('Login Sucessful Monu Raja...')
			time.sleep(1)
			os.system('python2 Monu.py') #Linking to main
		else:
			print('Wrong Password[!]')
			time.sleep(1)
			login()
	else:
		print('Wrong Username[!]')
		time.sleep(1)
		login()

def serial_keys():
	try:
		keys = open('Resgister.txt','r')
		login() 
	except (KeyError,IOError):
		pass
		LOGO()
		keys = raw_input('Enter 50 digit Serial Keys:~ ')
		if keys =='':
			print('Wrong Serial Keys')
			time.sleep(1)
			exit()
		elif keys =='G457-RT78-27GS-78YI-98T9-475T-2ET5-146G-JUH9-45RY-4H4DU-765R7' or keys =='G457RT7827GS78YI98T9475T2ET5146GJUH945RY4H4DU765R7':
			saved = open('Resgister.txt','w')
			saved.write('G457-RT78-27GS-78YI-98T9-475T-2ET5-146G-JUH9-45RY-4H4DU-765R7')
			saved.close()
			printing('Tool Register Sucessful..')
			login()
		else:
			print('Wrong Serial Keys')
			time.sleep(1)
			exit()
serial_keys()		
