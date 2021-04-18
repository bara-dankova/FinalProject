# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import the ./application/routes.py file
# from application import routes


# create a new instance of Flask and store it in app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymyssql://admin:M27awsdb@mg-aws-db.cedavxifa3ow.us-east-2.rds.amazonaws.com/first_aws_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# this is for the hidden tag in html forms
app.config['SECRET_KEY'] = 'SECRET_KEY'

# link app to the persistence layer
db = SQLAlchemy(app)