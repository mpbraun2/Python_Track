from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mysql = MySQLConnector(app, 'emaildb')

@app.route('/')
def index():
    query = "SELECT * FROM users"                           # define your query
    users = mysql.query_db(query)                           # run query with query_db()
    return render_template('email.html', users=users)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect("/")
    else:
        flash("Success!")
        print mysql.query_db("SELECT * FROM users")
        return redirect('/success')

app.run(debug=True)
