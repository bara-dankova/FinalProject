# import database connection from __init__.py
from application import db


class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
