from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dojo')
def index2():
    return render_template('index2.html', name="Mike P Braun", email="mpbraun2@email.com")
app.run(debug=True)
