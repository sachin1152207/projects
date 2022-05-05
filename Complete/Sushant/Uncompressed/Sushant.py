#coding=utf-8
#This Script is Written by Sachin Shrivastv
#Do not edit this code without permission
#If you edit this without permission then 
#You have to pay for this Code.
import os, sys, time
logo=""" \033[1;97m ___    _   _  ___    _   _  _____  _   _  _____ 
 (  _`\ ( ) ( )(  _`\ ( ) ( )(  _  )( ) ( )(_   _)
 | (_(_)| | | || (_(_)| |_| || (_) || `\| |  | |  
 `\__ \ | | | |`\__ \ |  _  ||  _  || , ` |  | |  
 ( )_) || (_) |( )_) || | | || | | || |`\ |  | |  
  \____)(_____)`\____)(_) (_)(_) (_)(_) (_)  (_)  """    
logo1=('══════════════════════════════════════════════════')     
def outing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


def password():
	os.system('clear')
	print (logo)  
	print (logo1)       
	print('             Owner   :- Badhßhah')
	print('             Author  :- Sachin Shrivastv')
	print('             Youtube :- Badhshah Hacker')
	print('             Whatsapp:- +977-9845844301')
	print(logo1)
	username= input(' Username:- ')
	if username =="":
		print('\033[1;91m[!] Invalid Username\033[1;97m')
		os.system('xdg-open https://www.youtube.com/channel/UCUltb-xVDLF6dtfgtPOBpuA')
		time.sleep(2)
		os.system('clear')
		password()
	elif username =="Admin" or username =="Im" or username =="Owner":
		outing(' Welcome back sir,')
		outing(' Hello sir, How are you Today..?')
		time.sleep(1)
		os.system('python2 Main.py')
	elif username =="Two_Brother" or username =="2BU": #Defalut username
		pswd= input(' Password:- ')
		if pswd =="":
			print('\033[1;91m[!]  Invalid Password\033[1;97m')
			os.system('xdg-open https://www.facebook.com/sachin.shrivastv.71')
			time.sleep(1)
			os.system('clear')
			password()
		elif pswd =="Shrivastvjee" or pswd =="Shreewastavjee": #Defalut pass
			outing(' Logged Successful as Sushant')
			os.system('python2 Main.py')
		else:
			print('\033[1;91m[!]  Invalid Password\033[1;97m')
			os.system('xdg-open https://www.facebook.com/sachin.shrivastv.71')
			time.sleep(1)
			os.system('clear')
			password()
	else:
		print('\033[1;91m[!] Invalid Username\033[1;97m')
		time.sleep(1)
		os.system('xdg-open https://www.youtube.com/channel/UCUltb-xVDLF6dtfgtPOBpuA')
		os.system('clear')	
		password()	
password()				                                                                   
                                             