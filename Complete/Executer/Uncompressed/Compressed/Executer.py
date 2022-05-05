import zlib, base64, os, sys
print("\033[1;92m")
os.system('figlet Execute Py')
path = raw_input("\033[1;93mEnter The File Path:- \033[1;97m")
try:
	file=open(path , 'r')
	text=file.read()
	file.close()
except (KeyError,IOError):
	print('File Not Found Error')
	os.system('exit')
	try:
		code=base64.b64encode(zlib.compress(text))
		code=code.decode('utf-8')
	except (NameError):
		os.system('exit')
	try:
		os.mkdir('Compressed')
	except OSError:
		pass
	print('\033[1;92mFile Compressed Successful!')
	fle = raw_input('Enter file name to save:- ')
	f=open(fle+ '.py', 'w')
	f.write('#This code is Compressed by Sachin Shrivastv'"\n")
	f.write('#Github:- Sac56'"\n")
	f.write('#Whatsapp:- +977-9845844301'"\n")
	f.write('#Youtube:- Badshah Hacker'"\n")
	f.write('import base64, zlib\nexec(zlib.decompress(base64.b64decode('"'" +code+ "'"')))')
	f.close()
	os.system('mv '+fle+'.py'' Compressed')
	view = raw_input("Do You Want View Compressed File(Y/N):- ")
	if view =="":
		print("Wrong Input")
	elif view =="Y":
		os.system('vi ''Compressed/'+fle+ '.py')
	elif view =="y":
		os.system('vi ''Compressed/'+fle+ '.py')
	elif view =="N":
		os.system('exit')
	elif view =="n":
		os.system('exit')
	else:
		os.system('exit')

	