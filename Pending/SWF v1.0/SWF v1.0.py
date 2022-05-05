#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To Sachin Shrivastv
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2021


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser

os.system('clear')
def typing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)
def banner():
	time.sleep(0.1)
	print("                          ,     \    /      ,")
	time.sleep(0.1)
	print("""                         / \    )\__/(     / \ """)
	time.sleep(0.1)
	print("""                        /   \  (_\  /_)   /   \   """)
	time.sleep(0.1)
	print('    <__________________/_____\__\@  @/___/_____\_________________>')
	time.sleep(0.1)
	print('     |                          |\../|                          |')
	time.sleep(0.1)
	print('     |                           \VV/                           |')
	time.sleep(0.1)
	print('     |                   \033[1;93mOwner:~  Badhshah\033[1;97m                      |')
	time.sleep(0.1)	
	print('     |                 \033[1;93mAuthor:~   Sachin Shrivastv\033[1;97m              |')
	time.sleep(0.1)
	print('     |                 \033[1;93mYoutube:~  Badhshah Hacker\033[1;97m               |')
	time.sleep(0.1)	
	print('     |__________________________________________________________|')
	time.sleep(0.1)
	print('''                 |    /\ /      \\\        \ /\    |''')
	time.sleep(0.1)
	print('                 |  /   V        ))        V   \  |')
	time.sleep(0.1)
	print('                 |/             //               \|')
	time.sleep(0.1)
	print('''                 `              V                 `''')
logo=('>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<')
def exit():
	time.sleep(0.1)
	os.system('exit')
def active():
	try:
		data=open('active','r').read()
		cast() #Pending To Home Screen
	except IOError:
		key = raw_input('Enter 30Digits Serial Keys To Activate This Exploit:- ').upper()
		if key =="":
			typing('Failed To Activate Exploit!!')
			os.system('rm -rf Conformed')
			exit()
		elif key =="M48O29N00U86S47A59C49H18I64N56":
			time.sleep(1)
			typing('Congratulations!, Exploit Has Been Activated Sucessfully...')
			file = open("active", 'w')
			file.write('Activated Tool, Congratulations You Are Superuser Of The Exploit')
			file.close()
			cast() #Pending To Home Screen
		else:
			print('Failed To Activate Exploit!!')
			os.system('rm -rf Conformed')
			exit()
def install():
	try:
		data=open('Conformed','r').read()
		icon()
	except IOError:
		os.system('clear')
		banner()
		print(logo)
		typing('The following terms and conditions apply to each user of this tool (The"FB Login Bot”). User acknowledges acceptance of these terms and conditions by accessing this Tool. If you do not accept, or disagree with, any of the terms and conditions, please do not use this Tools.Badhshah Hacker reserves the right to change these terms and conditions from time to time in its discretion. Revisions to the terms and conditions will be effective from the time they are posted on Github.')
		print(logo)
		conform = raw_input('Are you agreed with our terms and Condition(Y/N) :-').upper()
		if conform =="":
			exit()
		elif conform =="Y":
			file = open("Conformed", 'w')
			file.write('YES, I have conformed the terms and condition of this tools. if I have done any illegal activities with this tools. Then the devloper is not reponsiable for my mistake')
			file.close()
			icon()
		elif conform =="N":
			typing('To Run this Tools Please Conformed This Agreement')
			time.sleep(1)
			exit()
		elif conform =="EXIT":
			exit()
		else:
			exit()
def icon():
	os.system('clear')
	banner()
	typing(logo)
	active()
	








	
if __name__ == '__main__':
	install()