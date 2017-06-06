from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/users/<Mike>')
def show_user_profile(Mike):
	print Mike
        return render_template("user.html")
app.run(debug=True)