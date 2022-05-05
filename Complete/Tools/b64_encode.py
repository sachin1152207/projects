#utf-8
#Badhshah x Mr.Piece x Mr.Barnes
#Owner Badhshah
#Author Mr.Piece
#Coder Mr.Barnes 
import base64,os,sys
def main():
	os.system('cls')
	print("\tBase64 Encoding & Decoding")
	print("1~~~~~>>> Base64 Encode")
	print("2~~~~~>>> Base64 Decode")
	opt = input("Your Choice:- ")
	if opt =="1":
		data = input("Enter Decoded String:- ")
		b64encode(data)
	elif opt =="2":
		data = input("Enter Encoded String:- ")
		b64decode(data)
	else:
		print("Wrong Argument!")
		sys.exit()
def b64encode(data):
	data = data.encode('utf-8')
	base64_byte = base64.b64encode(data)
	base64_encode = base64_byte.decode('utf-8')
	print("Base64 Encoded Data:",base64_encode)
def b64decode(data):
	try:
		data = data.encode('utf-8')
		base64_byte = base64.b64decode(data)
		base64_decode = base64_byte.decode('utf-8')
		print("Base64 Decoded Data:",base64_decode)
	except:
		print("Bad String Data Input!")
		sys.exit()
if __name__ == '__main__':
	main()