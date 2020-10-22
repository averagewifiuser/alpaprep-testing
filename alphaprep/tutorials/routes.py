from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, send_file, session
from alphaprep.models import User, User_progress, User_streak, Subject_level, User_achievement
from flask_login import  login_user, current_user, logout_user, login_required
from alphaprep.quiz import shuffle
from alphaprep.util import filters, fxns, dbloader, token_fxn
from alphaprep.decorators import check_confirmed
from flask_mail import Message
import random
from datetime import datetime, timedelta
from collections import Counter 

tutorials = Blueprint('tutorials', __name__)


# all routes regarding tutorials


@check_confirmed  
@tutorials.route('/tutorialslanding', methods = ['GET', 'POST'])
def tutorials_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('tutorialslanding_final.html', title = 'Tutorials Landing Page')

 
@check_confirmed  
@tutorials.route('/englishlanding', methods = ['GET', 'POST'])
def english_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('english_landing.html', title = 'Tutorials Landing Page')

 
@check_confirmed  
@tutorials.route('/intsciencelanding', methods = ['GET', 'POST'])
def intscience_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('sciencelanding.html', title = 'Tutorials Landing Page')
    

@check_confirmed  
@tutorials.route('/cmathlanding', methods = ['GET', 'POST'])
def cmath_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('cmathlanding.html', title = 'Core Math Tutorials')



@check_confirmed  
@tutorials.route('/sociallanding', methods = ['GET', 'POST'])
def social_landing():
    if current_user.is_anonymous:
        flash('You must be logged in to access this page', 'warning')
        return redirect(url_for('main.login'))
    return render_template('sociallanding.html', title = 'Tutorials Landing Page')



@check_confirmed   
@tutorials.route('/tutorials', methods = ['GET', 'POST'])
def tutorial():
    subject = request.form['subject']
    topic = request.form['topic']
    
    
    videos = dbloader.load_videos(subject, topic)
    pdfs = dbloader.load_pdfs(subject, topic)    
    
    return render_template('tutorials_final.html',topic=topic,videos=videos, pdfs=pdfs,  title = 'Tutorials Page')


@tutorials.route('/return-file/', methods =['GET','POST'])
def return_file(): # to be able download the pdfs
    main = 'pdffiles/'
    file = request.form['file']
    
    file_path = main + file
    # the send_file function is in flask and aids us to download the pdf
    
    return send_file(file_path, attachment_filename = 'Tutorials.pdf')