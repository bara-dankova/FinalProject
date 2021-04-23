from application import db


class Contestant(db.Model):
    contestant_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(32), nullable=False)
    pronoun = db.Column(db.String(32), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    country = db.Column(db.String(32), nullable=False)
    songs = db.relationship("Song")
    blogs = db.relationship("Blog")


class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    contestant_id = db.Column(db.Integer, db.ForeignKey("contestant.contestant_id"), nullable=False)
    song_name = db.Column(db.String(64), nullable=False)


class Blog(db.Model):
    blog_id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.Date, nullable=False)
    contestant_id = db.Column(db.Integer, db.ForeignKey("contestant.contestant_id"), nullable=False)
    blog_views = db.Column(db.Integer, nullable=False)
    blog_title = db.Column(db.String(30), nullable=False)
    blog_text = db.Column(db.String(1000), nullable=False)

class Contact(db.Model):
    contact_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(30), nullable=False)
    message = db.Column(db.String(1000), nullable=False)

# 1. Models -- what tables and what columns
# 2. CRUD (create read update delete)
