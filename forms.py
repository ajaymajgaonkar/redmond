from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms import validators
from wtforms.validators import Email, DataRequired


class SignupForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired("First name is required")])
    last_name = StringField("Last Name", validators=[DataRequired("Last name is required")])
    email = StringField("Email", validators=[DataRequired("Email is required"), Email("Please enter valid email address")])
    password = PasswordField("Password", validators=[DataRequired("Password is required")])
    submit = SubmitField("Sign Up")


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Please specify your name")])
    email = StringField("Email", validators=[DataRequired("Email is required"), Email("Please enter valid email address")])
    message = TextAreaField("Message", validators=[DataRequired("Please write some message")])
    submit = SubmitField("Send")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Email is required"), Email("Please enter valid email address")])
    password = PasswordField("Password", validators=[DataRequired("Password is required")])
    submit = SubmitField("Login")

class TodoForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired("Email is required"), Email("Title cannot be left empty")])    
    submit = SubmitField("Add")
