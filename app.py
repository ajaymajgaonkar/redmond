from flask import Flask, jsonify, request, redirect, url_for, session
from flask import render_template
# from models import User
from forms import SignupForm, ContactForm, LoginForm
from flask_mongoalchemy import MongoAlchemy
import os

app = Flask(__name__)
app.secret_key = "developmentkey"

app.config['MONGOALCHEMY_DATABASE'] = 'library'
app.config['MONGOALCHEMY_CONNECTION_STRING'] = "mongodb://admin:admin123@ds155718.mlab.com:55718/library"#os.environ.get('MONGODB_URI')
db = MongoAlchemy(app)


class User(db.Document):
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.StringField()
    password = db.StringField()


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
            user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data,
                        password=form.password.data)
            user.save()
            session['username'] = form.email.data
            return redirect(url_for('index'))
    elif request.method == "GET":
        return render_template("Signup.html", form=form)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template("Contact.html", form=form)
        else:
            redirect(url_for('index'))
    elif request.method == "GET":
        return render_template("Contact.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate() == False:
            return render_template("Login.html", error='Please fill username and password', form=form)
        else:
            login_user = User.query.filter(User.email == form.email.data).first()
            if login_user:
                if login_user.password == form.password.data:
                    session['username'] = form.email.data
                    return render_template("Index.html")
            return render_template("Login.html", error='Login failed', form=form)
    return render_template("Login.html", form=form)


@app.route("/logout")
def logout():
    session['username'] = ''
    return render_template("Index.html")


@app.route("/users")
def users():
    return jsonify([o.email + " | " + o.password for o in User.query.all()])


if __name__ == "__main__":
    app.run(debug=True)
