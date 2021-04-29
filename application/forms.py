from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField


class ContactUsForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    subject = StringField('Subject')
    message = TextAreaField('Message')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    name = StringField('Name')
    text = TextAreaField('Text')
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    username = EmailField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name')
    username = EmailField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Register')
