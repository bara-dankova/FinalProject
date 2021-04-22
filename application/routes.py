from flask import render_template, request, url_for
from application import app, db
from application.forms import Contact_us_form

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')


# create url for a particular blog post
@app.route('/blogpost')
def blogpost1():
    return render_template('blogpost.html', title='First Blog Post')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    error=''
    form = Contact_us_form()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        subject = form.subject.data
        message = form.message.data
        if len(first_name)==0 or len(last_name)==0:
            error = 'Please fill in both your first and last name'
        elif len(message)==0:
            error= 'Please type your message in the message box'
        else:
            return render_template('thankyou.html', title='Thank you')
        # return """
        # <p>
        # {}
        # {}
        # {}
        # {} </p>
        # """.format(first_name, last_name, subject, mail)
    return render_template('contact.html', title='Contact Us!', message=error, form=form)