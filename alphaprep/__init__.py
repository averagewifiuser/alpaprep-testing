from flask import Flask  # importing flask
from flask_sqlalchemy import SQLAlchemy # helps to use the database as Objects
from flask_bcrypt import Bcrypt # for hashing the passwords
from flask_login import LoginManager #This is an in-built thing for flask, helps to manage the logining in and out of users
from flask_mail import Mail # a special diswan for sending mails through flasks, nice right?
import os # imported so we can hide sensitive info



app = Flask(__name__) # yaay the instance our Flask App
app.config['SECRET_KEY'] = os.environ['ALPHA_SECRET_KEY'] # so our site is cookies are secured
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['ALPHA_URI'] # location for database, note we use mysql and sqlachemy interchangebly. Interesting stuff really, see notes at end of page

app.config['SERVER_NAME'] = '127.0.0.1:5000' # it is a local server so yah, we dix
app.config['SECURITY_PASSWORD_SALT'] = os.environ['SECURITY_PASSWORD_SALT'] # This is for confirmation emails, I'll explain later.
db = SQLAlchemy(app) # sqlachemy database instance
bcrypt = Bcrypt(app) # instance of our hashing passwords
login_manager = LoginManager(app) #instance of the login manager, it is initialized for our app
login_manager.login_view = 'main.login'  # login route for login required pages
# the login is the function name of our routes for login (you barb?)
login_manager.login_message_category = 'info' # makes the messages a bit nicer

app.config['MAIL_SERVER'] = 'smtp.gmail.com'      # using google's mail service
app.config['MAIL_PORT'] = 465 # well this is the mail port
app.config['MAIL_USE_TL'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ['ALPHA_MAIL']
app.config['MAIL_PASSWORD'] = os.environ['ALPHA_MAIL_PASSWORD']
mail = Mail(app) # instance of the mail app

from alphaprep import routes
from alphaprep.main.routes import main
from alphaprep.users.routes import users
from alphaprep.tests.routes import tests
from alphaprep.tutorials.routes import tutorials

app.register_blueprint(main) 
app.register_blueprint(users)
app.register_blueprint(tests)
app.register_blueprint(tutorials)


# it is here because of the sequence of the executing of instructions
# it would avoid anything basa basa


# each class is its own table in the database
# everything has been separated into packages, modules and files


'''
So we use Sqlachemy and at the same time mysql.
Our SQLAlchemy URI is intialized to our mysql database, so we can actually use both at the same time.
We can have the full functionality of the objects for alchemy and the experience we have from mysql.


So mysql is mainly for the questions, see 'dbloader' to see its implementation
the rest is mainly handled by sqlachemy or so. yeah


'''