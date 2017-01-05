from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import validators
from wtforms.validators import Required, Email


class SignupForm(FlaskForm):
    first_name = StringField("First Name", validators=[Required("First name is required")])
    last_name = StringField("Last Name", validators=[Required("Last name is required")])
    email = StringField("Email", validators=[Required("Email is required"), Email("Please enter valid email address")])
    password = PasswordField("Password", validators=[Required("Password is required")])
    submit = SubmitField("SignUp")

