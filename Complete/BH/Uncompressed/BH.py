import os, sys, time
os.system('clear')
logo="""  .----------------.  .----------------. 
 | .--------------. || .--------------. |
 | |   ______     | || |  ____  ____  | |
 | |  |_   _ \    | || | |_   ||   _| | |
 | |    | |_) |   | || |   | |__| |   | |
 | |    |  __'.   | || |   |  __  |   | |
 | |   _| |__) |  | || |  _| |  | |_  | |
 | |  |_______/   | || | |____||____| | |
 | |              | || |              | |
 | '--------------' || '--------------' |
 '----------------'  '----------------' """
logo1=(" <<<<<<<<<<<<<<<<<<<==>>>>>>>>>>>>>>>>>>>")
def printing(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00.1)
def login():
	print(logo)
	print(logo1)
	print('         Owner:-    Badhshah')
	print('         Author:-   Sachin Shrivastv')
	print('         Youtube:-  Badhshah Hacker')
	print('         Whatsapp:- +977-9845844301')
	print(logo1)
	username = raw_input(' Enter Username:- ')
	if username =="":
		print('[!] Invalid Input')
		os.system('xdg-open https://www.youtube.com/channel/UCUltb-xVDLF6dtfgtPOBpuA')
		time.sleep(1)
		os.system('clear')
		login()
	elif username =="Badhshah": #Default Username
		password = raw_input(' Enter Password:- ')
		if password =="":
			print('[!] Invalid Input')
			os.system('xdg-open https://www.facebook.com/Badhshah-Hacker-119051486545625')
			time.sleep(1)
			os.system('clear')
			login()
		elif password =="Hacker": #Default Password
			printing(' Logged Successful as Badhshah')
			os.system('python2 data.py') #Main #File
		else:
			print('[!] Invalid Input')
			os.system('xdg-open https://www.facebook.com/Badhshah-Hacker-119051486545625') 
			time.sleep(1)
			os.system('clear')
			login()
	else:
		print('[!] Invalid Input')
		os.system('xdg-open https://www.youtube.com/channel/UCUltb-xVDLF6dtfgtPOBpuA')
		time.sleep(1)
		os.system('clear')
		login()	
login()

