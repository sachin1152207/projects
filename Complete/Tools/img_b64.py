import base64,os,sys,time
from datetime import datetime
tm = datetime.now()
cr_time = tm.strftime('%H:%M:%S')
def main():
	os.system('cls')
	print('<<------------------------------>>')
	print('      Image Encoder & Decoder')
	print('	Mr.Piece x Badhshah')
	print('<<------------------------------>>')
	print("1~~~~>> Img Encode")
	print("2~~~~>> Img Decode")
	print("0~~~~>> Exit")
	opt = input("Your Choice:~ ")
	if opt == "1":
		img_path = input("Enter File Path or File Name:- ")
		img_encode(img_path)
	elif opt == "2":
		txt_path = input("Enter Txt File Path or File Name:- ")
		img_decode(txt_path)
	elif opt == "3":
		print("""This is open source image encoding decoding python script. Working on Base64 encoding lib in python
Devloped by 2004 Team in Nepal with all legal process
Owner : Badhshah
Author: Sachin Shrivastv
Coder : Mr.Barnes
Github: sachin152207 """)
		input("Press Enter to Continue...")
		main()
	elif opt == "0" or "exit":
		sys.exit()
	else:
		print("Invalid Argument!")
		main()
def img_encode(img_en):
	try:
		with open(img_en, 'rb') as img_data:
			img_file = img_data.read()
			img_b64 = base64.b64encode(img_file)
			img_utf = img_b64.decode('utf-8')
			print("Image Has Been Encoded Sucessfull, Encoded Length Size:",len(img_utf))
	except:
		print("Directory or File Not Found 404")
		sys.exit()
	img_out = img_utf.encode('utf-8')
	save = open(img_en+ '.txt', 'wb')
	save.write(img_out)
	save.close()
def img_decode(img_de):
	try:
		with open(img_de, 'rb') as b64_img:
			b64_pic = b64_img.read()
			decoded_img = base64.decodebytes(b64_pic)
			print("File Decoded Sucessfull at:",cr_time)
	except:
		print("Directory or File Not Found 404")
		sys.exit()
	file_name = input("Enter File Name With Extension To Save:~ ")
	if file_name == "":
		print("Failed To Save Decoded Data!")
		sys.exit()
	else:
		with open(file_name, 'wb') as decode_img:
			decode_img.write(decoded_img)
			decode_img.close()
if __name__ == '__main__':
	main()