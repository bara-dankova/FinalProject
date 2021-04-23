from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class Contact_us_form(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    subject = StringField('Subject')
    message = StringField('message')
    submit = SubmitField('Submit')