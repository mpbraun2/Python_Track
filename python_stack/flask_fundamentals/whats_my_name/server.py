from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process')
def index2():
    return render_template('index2.html')
app.run(debug=True)