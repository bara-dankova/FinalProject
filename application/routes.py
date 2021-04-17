from flask import render_template, request
from application import app, db


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home Page')


# create url for a particular blog post
@app.route('/blogpost')
def blogpost1():
    return render_template('blogpost.html', title='First Blog Post')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us!')