import requests
import sys, os
url = sys.argv[1]
file = open("link_list.txt", 'r').readlines()
header = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41'}
found = []
notfound = []
logo = """               # # # # # # # # # # # # # # # #
               #       Admin Pager Finder    #
               #         Group:~ 2004        #
               #       Owner:~ Badhshah      #
               #      Author:~ Mr.Piece      #
               #       Code :~ Mr.Barnes     #
               # # # # # # # # # # # # # # # #"""
os.system('clear')
print(logo)
print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
try:
	for line in file:
		line = line.replace("\n", "")
		link = url +"/"+ line
		http = requests.get(url=link, headers=header)
		code = http.status_code
		if code =="404" or "301":
			if not "Page not found" in str(http.content):
				print("[+] Page Found: "+link)
				found.append(link)
			else:
				print("[-] Page Not Found: "+link)
				notfound.append(link)
		else:
			print("[-] Page Not Found: "+link)
			notfound.append(link)
except (KeyboardInterrupt):
	pass
print("}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{")
print("Scaning Complete....Page Found[200]: "+str(len(found))+", Page Not Found[404]: "+str(len(notfound)))