from flask import render_template, url_for, flash, redirect, request, send_file, session
from alphaprep import app, db, bcrypt, mail
from alphaprep.models import User
from flask_mail import Message
from datetime import datetime, timedelta


# this function is for sending messages to the user when they have been off for a while
# you need internet to run it or your app wont run adaaaalll






# user session expires after 5 hours
# basically automatically logs the user out
@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=300)	
    
    
@app.route("/mobile-error", methods = ['GET'])
def mobile_response():
    return render_template('mobileresponse.html')
            
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('405.html'), 405

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
    