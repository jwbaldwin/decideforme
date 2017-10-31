from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)
#webcode = open('webcode.html').read()
#Use:
#
# export FLASK_APP=main.py
# flask run
@app.route('/')
def main(): 
    return render_template('main.html') 

@app.route('/pick', methods=['POST'])
def pick():
	return randint(1,5)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)