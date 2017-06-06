
from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

app.secret_key = 'ThisIsSecret'

def startCount():
    try:
        session["count"]
    except KeyError:
        session["count"] = 1

@app.route('/')
def homepage():
    startCount()
    return render_template('index.html', count = session["count"])

@app.route('/increment', methods=['GET'])
def incrementByOne():
    session["count"] += 1
    return redirect('/')

@app.route('/ninja1', methods=['GET'])
def incrementByTwo():
    session["count"] += 2
    return redirect('/')

@app.route('/ninja2', methods=['GET'])
def resetCounter():
    session["count"] = 1
    return redirect('/')


app.run(debug=True)
