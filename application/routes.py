import sqlalchemy
from flask import render_template, request, url_for, redirect, session
from application import app, db
from application.forms import *
from application.models import *
from application.password import hash_password, check_password
from datetime import datetime


@app.route('/')
@app.route('/home')
def home():
    user = session["user"] if "user" in session else None
    blogs = Blog.query.all()
    contestant = Contestant
    song = Song
    print(user)
    return render_template('home.html', title='Home Page', user=user, blogs=blogs,
                           contestant=contestant, song=song, activityLeader='',
                           activityContact = '', activityHome='active')


# create url for a particular blog post
@app.route('/blogpost/<int:contestant_id>', methods=['GET', 'PUT'])
def blogpost1(contestant_id):
    user = session["user"] if "user" in session else None
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
    return render_template('blogpost.html', title=contestant.first_name, user=user, blog=blog,
                           contestant=contestant, song=song,
                           comments=comments, form=CommentForm(),
                           comment_form_url=f"/blogpost/{contestant.contestant_id}/comment")


@app.route('/blogpost/<int:contestant_id>/comment', methods=['POST'])
def add_comment(contestant_id):
    user = session["user"] if "user" in session else None
    form = CommentForm()

    name = form.name.data
    text = form.text.data
    time = datetime.utcnow()


    blog = Blog.query.filter_by(contestant_id=contestant_id).first()

    comment = Comment(time=time, text=text, blog_id=blog.blog_id,  username=name)
    db.session.add(comment)
    db.session.commit()

    return redirect(f"/blogpost/{contestant_id}")


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    user = session["user"] if "user" in session else None
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
    return render_template('contact.html', title='Contact Us!', user=user, message=error, form=form,
                           activityLeader='', activityContact='active', activityHome='')


@app.route('/leaderboard')
def leaderboard():
    user = session["user"] if "user" in session else None
    songs_list = Song.query.all()
    contestants_list = Contestant.query.all()

    # sort functions
    return render_template('leaderboard.html', title='Leaderboard',
                           songs_list=songs_list,
                           contestants_list=contestants_list,
                           song=Song,
                           contestant=Contestant, user=user,
                           activityLeader='active', activityContact = '', activityHome='')


@app.route('/blog/like/<int:contestant_id>', methods=['GET', 'PUT'])
def likeblog(contestant_id):
    user = session["user"] if "user" in session else None
    liked_blog = Blog.query.filter_by(contestant_id=contestant_id).first()

    if liked_blog.blog_likes is not None:
        setattr(liked_blog,'blog_likes', liked_blog.blog_likes+1)
        db.session.commit()
    else:
        setattr(liked_blog, 'blog_likes', 1)
        db.session.commit()
    return redirect(f"/blogpost/{contestant_id}")


@app.route('/song/like/<int:contestant_id>', methods=['GET', 'PUT'])
def likesong(contestant_id):
    user = session["user"] if "user" in session else None
    liked_song = Song.query.filter_by(contestant_id=contestant_id).first()

    if liked_song.song_likes is not None:
        setattr(liked_song,'song_likes', liked_song.song_likes+1)
        db.session.commit()
    else:
        setattr(liked_song, 'song_likes', 1)
        db.session.commit()
    return redirect("/leaderboard")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        user = session["user"] if "user" in session else None
        form = RegisterForm()
        return render_template('register.html', title='Register', user=user, form=form)
    else:
        try:
            form = RegisterForm()

            name = form.name.data
            username = form.username.data
            password = form.password.data

            user = User(name=name, username=username, password_hash=hash_password(password.encode()))
            db.session.add(user)
            db.session.commit()
        except sqlalchemy.exc.IntegrityError:
            return render_template('register.html',
                                   title='Register',
                                   form=form,
                                   message='This email address has already been used. Please use another email address')
        else:
            session["user"] = {"name": user.name}
        return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        user = session["user"] if "user" in session else None
        form = LoginForm()

        return render_template('login.html', title='Login', user=user, form=form)
    else:
        form = LoginForm()

        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and check_password(password.encode(), user.password_hash.encode()):
            session["user"] = {"name": user.name}

        return redirect("/")


@app.route('/logout', methods=['GET'])
def logout():
    session.pop("user")

    return redirect("/")