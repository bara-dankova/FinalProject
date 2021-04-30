from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class ContactUsForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    subject = StringField('Subject')
    message = StringField('message')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    name = StringField('Name')
    text = StringField('Text')
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    search = StringField('Search')
    submit = SubmitField('Search')
