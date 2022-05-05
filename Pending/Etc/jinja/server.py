from flask import Flask, request, render_template
import json

id = json.load(open('contacts.json', 'r'))
'''
app = Flask(__name__)

@app.route('/')
def index():
	return "Hello World"

@app.route('/dashboard')
def dashboard():
	return render_template('index.html', data=data['data'])
	
app.run(debug=True)
'''

for naam in id['data']:
	n = naam['name']
	print(n)
