from flask import Flask
from flask import request
from flask import render_template
import requests
import financebot

app = Flask(__name__)

response = None
all_msgs = []
def chat_messages(msg_list):
    html = ''
    html += '<table id="chatbox">\n'
    for msg in msg_list:
        html += '<tr><td>\n'
        html += '</td><td>'.join(msg)
        html += '\n'
        html += '</td></tr>\n'
    html += '</table>'
    return html

@app.route('/')
def chat():
    global all_msgs
    global response
    bot_message, response = financebot.evaluate_message('', response)
    #print bot_message
    all_msgs = [bot_message] + all_msgs
    return render_template("index.html", html_table = chat_messages(all_msgs))

@app.route('/', methods=['POST'])
def chat_post():
    global all_msgs
    global response
    message = request.form['message']
    bot_message, response = financebot.evaluate_message(message, response)
    #print message, bot_message
    all_msgs = [['User', str(message)]] + all_msgs
    all_msgs = [bot_message] + all_msgs
    return render_template("index.html", html_table = chat_messages(all_msgs))

if __name__ == '__main__':
    app.debug = True
    app.run()