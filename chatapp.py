from flask import Flask
from flask import request
from flask import render_template
import requests
import financebot

app = Flask(__name__)

def chat_messages(msg_list):
	html = ''
	html += '<table>\n'
  	for msg in msg_list:
    	html += '<tr><td>\n'
    	html += '</td><td>'.join(msg)
    	html += '\n'
    	html += '</td></tr>\n'
  	html += '</table>'
  	return html

@app.route('/')
def chat():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def chat_post():
	message = request.form['message']
	return message

if __name__ == '__main__':
	app.debug = True
	app.run()