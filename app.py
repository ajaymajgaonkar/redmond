from flask import Flask, jsonify, request, redirect, url_for, session
from flask import render_template
# from models import User
from forms import SignupForm, ContactForm, LoginForm, TodoForm
from flask_mongoalchemy import MongoAlchemy
from flask_mongoalchemy import fields
import os
from datetime import datetime

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

class Item(db.Document):
    title = db.StringField()
    status = db.StringField()
    created_date = db.DateTimeField()
    created_by = db.StringField()

@app.route("/")
def index():
    return render_template("Index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if request.method == "POST":
        if form.validate() == False:
            return render_template("Signup.html", form=form, error='All fields are required')
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
                    return redirect(url_for('todo'))
            return render_template("Login.html", error='Login failed', form=form)
    return render_template("Login.html", form=form)

@app.route("/todo", methods=["GET", "POST"])
def todo():
    form = TodoForm()
    if 'username' in session:
        items = Item.query.filter(Item.created_by == session['username']).all()
        if request.method == "POST":
            if form.validate() == False:
                return render_template("Todo.html", error='Please fix errors and try again', form=form, items=items)
            else:
                item = Item(
                    title=form.title.data, 
                    status=form.status.data,
                    created_date = datetime.utcnow(), 
                    created_by = session['username'])
                item.save()
                items.append(item)
                return render_template("Todo.html", form=form, items=items)
        elif request.method == "GET":                
            return render_template("Todo.html", items=items, form=form)
    else:
        return redirect(url_for('login'))

@app.route("/deleteItem", methods=["POST"])
def deleteItem():
    item_id = request.form['data']
    item = Item.query.filter(Item.mongo_id == item_id).first()
    item.remove()
    return redirect('todo')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return render_template("Index.html")


@app.route("/users")
def users():
    return jsonify([o.email + " | " + o.password for o in User.query.all()])


if __name__ == "__main__":
    app.run(debug=True)
