#python flask Website
#Herouku Hosted Webiste

from flask import Flask, request, render_template, jsonify, url_for, redirect, session
import smtplib
from datetime import datetime
import time

'''server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("lazycoder58@gmail.com", "lazycoder_blog8845")
sender = "lazycoder58@gmail.com"
receiver = "sachinshrivastv152207@gmail.com"'''

app = Flask(__name__)
app.secret_key = '15285722f9def45c091725aee9c387cb'
@app.errorhandler(404)
def error(e):
	return render_template('error.html'), 500

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
	if request.method == "POST":
		name = request.form.get('name')
		email = request.form.get('email')
		msg = request.form.get('message')
		date = str(datetime.fromtimestamp(time.time()))
		
		message = """From: Blogs Website
		To: sachinshrivastv152207@gmail.com
		Subject: Contact form Message. 
		New contact message form blog.

		Name: """+name+"""
		Email: """+email+"""
		Date: """+date+"""
		Message: """+msg+"""
		"""
		
		server.sendmail(sender, receiver, message)
		server.quit()
		return redirect(url_for('index'))
	else:
		 return redirect(url_for('index'))
		 
@app.route('/login', methods=['POST', 'GET'])
def login():
	if 'user' in session and session['user'] == "sachin@login":
		return redirect(url_for('dashboard'))
	elif request.method == "POST":
		username = request.form.get('username')
		password = request.form.get('password')
		if username == "sachin@login" and password == "sachin@home":
			session['user'] = "sachin@login"
			return redirect(url_for('dashboard'))
		else:
			return render_template('login.html'), 401
	else:
		 return render_template('login.html'), 200
		 
@app.route('/dashboard')
def dashboard():
	if 'user' in session and session['user'] == "sachin@login":
		return render_template('dashboard.html'), 200
	else:
		return render_template('login.html'), 200
@app.route('/logout')
def logout():
	session.pop('user', None)
	return render_template('login.html'), 200
	
if __name__ == '__main__':
	app.run(debug=False, host='0.0.0.0')