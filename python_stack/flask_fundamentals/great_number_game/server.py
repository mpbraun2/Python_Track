
import random
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

@app.route('/')
def homepage():
    startcount()
    return render_template('index.html', count=session['count'])

def startcount():
    session['count'] = random.randrange(0, 101)

@app.route('/wasitclose', methods=['post'])
def checker():
    session['guess'] = request.form['guess']
    if session['count'] < session['guess']:
        return render_template('toohigh.html')
    if session['count'] > session['guess']:
        return render_template('toolow.html')
    if session['count'] == session['guess']:
        return render_template('correct.html')


app.run(debug=True)
