from flask import render_template, request, url_for, redirect, session
from application import app, db
from application.forms import *
from application.models import *
from datetime import datetime


@app.route('/')
@app.route('/home')
def home():
    blogs = Blog.query.all()
    contestant = Contestant
    song = Song
    return render_template('home.html', title='Home Page', blogs=blogs, contestant=contestant, song=song)


# create url for a particular blog post
@app.route('/blogpost/<int:contestant_id>', methods=['GET', 'PUT'])
def blogpost1(contestant_id):
    blog = Blog.query.filter_by(contestant_id=contestant_id).first()
    contestant = Contestant.query.filter_by(contestant_id=contestant_id).first()

    song = Song.query.filter_by(contestant_id=contestant_id).first()
    comments = Comment.query.filter_by(blog_id=blog.blog_id).all()
    if blog.blog_views is not None:
        setattr(blog, 'blog_views', blog.blog_views + 1)
        db.session.commit()
    else:
        setattr(blog, 'blog_views', 1)
        db.session.commit()
    # to query contestants by name in URL and find the appropriate blog post
    # contestant = Contestant.query.all(name_from_url)
    return render_template('blogpost.html', title=contestant.first_name, blog=blog, contestant=contestant, song=song,
                           comments=comments, form=CommentForm(),
                           comment_form_url=f"/blogpost/{contestant.contestant_id}/comment")


@app.route('/blogpost/<int:contestant_id>/comment', methods=['POST'])
def add_comment(contestant_id):
    form = CommentForm()

    name = form.name.data
    text = form.text.data
    time = datetime.utcnow()

    print(name, text, time)

    blog = Blog.query.filter_by(contestant_id=contestant_id).first()

    comment = Comment(time=time, text=text, blog_id=blog.blog_id)
    db.session.add(comment)
    db.session.commit()

    return redirect(f"/blogpost/{contestant_id}")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    error = ''
    form = ContactUsForm()
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
                           contestant=Contestant)


@app.route('/blog/like/<int:contestant_id>', methods=[ 'GET', 'PUT'])
def likeblog(contestant_id):
    liked_blog = Blog.query.filter_by(contestant_id=contestant_id).first()

    if liked_blog.blog_likes is not None:
        setattr(liked_blog,'blog_likes', liked_blog.blog_likes+1)
        db.session.commit()
    else:
        setattr(liked_blog, 'blog_likes', 1)
        db.session.commit()
    return blogpost1(contestant_id)


# stillworking on connecting this to the right song
@app.route('/song/like/<int:contestant_id>', methods=['GET', 'PUT'])
def likesong(contestant_id):
    liked_song = Song.query.filter_by(contestant_id=contestant_id).first()

    if liked_song.song_likes is not None:
        setattr(liked_song,'song_likes', liked_song.song_likes+1)
        db.session.commit()
    else:
        setattr(liked_song, 'song_likes', 1)
        db.session.commit()
    return leaderboard()
