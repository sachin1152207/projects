#coding=utf-8
#This code Credits goes to Sachin Shrivastv
#This Tool is for Educational Purpose
#You were agree with our all terms and condition
#Before using our tools
#Note 45+ try on Single ip then ip will ban automatic
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063')]
os.system('clear')
def printing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.008)
def banner():
	print("                       ,     \    /      ,")
	print("""                      / \    )\__/(     / \ """)
	print("""                     /   \  (_\  /_)   /   \   """)
	print(' <__________________/_____\__\@  @/___/_____\_________________>')
	print('  |                          |\../|                          |')
	print('  |                           \VV/                           |')
	print('  |                         \033[1;93mTrack IP  \033[1;97m                       |')	
	print('  |                \033[1;93mAuthor:~   Sachin Shrivastv\033[1;97m               |')
	print('  |                \033[1;93mYoutube:~  Badhshah Hacker\033[1;97m                |')	
	print('  |__________________________________________________________|')
	print('''              |    /\ /      \\\        \ /\    |''')
	print('              |  /   V        ))        V   \  |')
	print('              |/             //               \|')
	print('''              `              V                 `''')
logo=('>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<')

def exit():
	os.system('exit')
def install():
	try:
		data=open('Conformed','r').read()
		main()
	except IOError:
		os.system('clear')
		banner()
		print(logo)
		print('The following terms and conditions apply to each user of this tool (The"FB Login Bot”). User acknowledges acceptance of these terms and conditions by accessing this Tool. If you do not accept, or disagree with, any of the terms and conditions, please do not use this Tools.Badhshah Hacker reserves the right to change these terms and conditions from time to time in its discretion. Revisions to the terms and conditions will be effective from the time they are posted on Github.')
		print(logo)
		conform = raw_input('Are you agreed with our terms and Condition(Y/N) ').upper()
		if conform =="":
			exit()
		elif conform =="Y":
			file = open("Conformed", 'w')
			file.write('YES, I have conformed the terms and condition of this tools. if I have done any illegal activities with this tools. Then the devloper is not reponsiable for my mistake')
			file.close()
			main()
		elif conform =="N":
			print('To Run this Tools Please Conformed This Agreement')
			time.sleep(1)
			exit()
		else:
			exit()
def main():
	os.system('clear')
	time.sleep(0.5)
	banner()
	print(logo)
	print('{1}~~~~~~> Track Your IP')
	print('{2}~~~~~~> Track Target IP')
	print('{0}~~~~~~> Exit')
	choose = raw_input('Select Your Choice:~ ')
	if choose =="":
		print('Invalid Input')
		time.sleep(0.5)
		main()
	elif choose =="1":
		own_ip()
	elif choose =="2":
		main()
	elif choose =="0":
		time.sleep(1)
		exit()
	else:
		print('Invalid Input')
		time.sleep(0.5)
		main()
def own_ip():
	os.system('clear')
	banner()
	print(logo)
	printing("Loading info...")
	try:
		ip = requests.get('http://ip-api.com/json/?fields=66318303')
		a = json.loads(ip.text)
		b = a['query']
		c = a['status']
		d = a['continent']
		e = a['continentCode']
		f = a['country']
		g = a['countryCode']
		h = a['region']
		i = a['regionName']
		j = a['city']
		k = a['lat']
		l = a['lon']
		m = a['timezone']
		n = a['offset']
		o = a['currency']
		p = a['isp']
		q = a['org']
		r = a['asname']
		s = a['mobile']
		t = a['proxy']
		u = a['hosting']
		print('Status:- \033[1;92m')+c
		print('Your IP Address:- ')+b
		print('Continent:- ')+d
		print('Continent Code:- ')+e
		print('Country:- ')+f
		print('Country Code:- ')+g
		print('Region:- ')+h
		print('Region Name:- ')+i
		print('City:- ')+j
		print('Latitude:- ')+k
		print('Longitude:- ')+l
		print('Time Zone:- ')+m
		print('Offeset:- ')+n
		print('Currency:- ')+o
		print('ISP:- ')+p
		print('Organzation:- ')+q
		print('Asname:- ')+r
		print('Proxy:- ')+s
		print('Mobile:- ')+t
		print('Hosting ')+u
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		exit()
		
		
	
	
	
	
if __name__ == '__main__':
	install()
