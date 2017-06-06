from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def index2():
    return render_template('ninjas.html')

@app.route('/dojo/new')
def index3():
    return render_template('dojos.html')
app.run(debug=True)