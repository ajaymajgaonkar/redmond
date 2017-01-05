from flask import Flask, jsonify, request, redirect, url_for
from flask import render_template
from models import User
from forms import SignupForm


app = Flask(__name__)
app.secret_key = "developmentkey"

@app.route("/")
def index():
	return render_template("Index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
	form = SignupForm()
	if request.method == "POST":
		if form.validate() == False:
			return render_template("Signup.html", form=form)
		else:
			redirect(url_for('index'))
	elif request.method == "GET":
		return render_template("Signup.html", form=form)



if __name__=="__main__":
	app.run(debug=True)