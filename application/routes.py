from flask import render_template, request, url_for
from application import app, db
from application.forms import Contact_us_form
from application.models import Contact, Song, Contestant


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
    error = ''
    form = Contact_us_form()
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        subject = form.subject.data
        message = form.message.data
        if len(first_name) == 0 or len(last_name) == 0:
            error = 'Please fill in both your first and last name'
        elif len(message) == 0:
            error = 'Please type your message in the message box'
        else:
            message_received = Contact(first_name=first_name, last_name=last_name, subject=subject, message=message)
            db.session.add(message_received)
            db.session.commit()
            return render_template('thankyou.html', title='Thank you')
        # return """
        # <p>
        # {}
        # {}
        # {}
        # {} </p>
        # """.format(first_name, last_name, subject, mail)
    return render_template('contact.html', title='Contact Us!', message=error, form=form)


@app.route('/leaderboard')
def leaderboard():

    songs_list = Song.query.all()
    contestants_list = Contestant.query.all()

    # sort functions
    return render_template('leaderboard.html', title='Leaderboard',
                           songs_list=songs_list,
                           contestants_list=contestants_list,
                           song=Song,
                           contestant=Contestant,
    )

