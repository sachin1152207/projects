#utf-8
#!/usr/bin/env python
#The Coding Credits Goes To Our Respected Devloper
#Mr. Piece (Sachin Shrivastv)
import argparse
import sys 
import socket 
import time as tm
import os
from datetime import datetime 
os.system('clear')
parser = argparse.ArgumentParser(description='Python Port Scanner Devloped By Mr.Piece')
parser.add_argument('host', help= 'Enter Target To Scan Open Port')
args = parser.parse_args()
target = (args.host)
time = datetime.now()
print('-'*56)
print('   Port Scaning Started On:~',time)
print('-'*56)
try:
    for port in range(1,65535): 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
        result = s.connect_ex((target,port)) 
        if result ==0: 
            print(" Port {}    Open".format(port)) 
        s.close()       
except KeyboardInterrupt:
	print("Port Scaning Has Been Stopped By User")
	tm.sleep(1)
	os.system('exit')
except socket.gaierror:
	print('Host Could Not Resloved. Exiting')
	tm.sleep(1)
	os.system('exit')
except socket.erorr:
	print("Couldn't Connect To Server")
	tm.sleep(1)
	os.system('exit')
	
time2 = datetime.now()
total = time2 - time
print('-'*56)
print("       Port Scanned Successful In:~", total)
print('-'*56)