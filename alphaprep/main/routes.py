from flask import render_template, url_for, flash, redirect, request, send_file, session
from alphaprep import app, db, bcrypt
from alphaprep.models import User, User_progress, User_streak, Subject_level, User_achievement
from flask_login import  login_user, current_user, logout_user, login_required
from datetime import timedelta, datetime
from alphaprep.util import filters, fxns, token_fxn, dbloader
from alphaprep.users.forms import LoginForm
from alphaprep.decorators import check_confirmed
from flask import Blueprint

main = Blueprint('main', __name__)

# routes for all the main stuff, they are not really related to a specific part
'''   
NOTE: THE COMMENTS ARE ACCORDING TO HOW WE FELT! SOME ARE SERIOUS, SOME MAY LOOK JOVIAL. PLEASE TAKE ALL SERIOUSLY.
WE TYPED THIS IN CAPS NOT TO BE RUDE BUT TO MAKE SURE YOU READ IT WELL.

THANKS

- BACK END
'''


''' The email functions work but without internet you will get a gaierror: errno 1011. So remember to connect the internet
and make sure everything is working properly'''

'''

The render_template, you see some variables being put there, they help us you know put variables on the web page
I hope you get this explanation

'''


    
    
    

@main.route("/")
@main.route("/home")
def home():
    return redirect(url_for('main.login'))

@main.route("/bugs", methods=['GET', 'POST'])
def bugs():
    
    if request.method == 'POST':
        report = request.form['report']
        dbloader.load_bug_report(report)
        flash("Thank You! Our team will get right on fixing the issues you've reported. :)", 'success')
    return render_template('bugs.html')

@main.route("/index", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.dashboard'))
    
    
    form = LoginForm() # instance of our login form from forms, you should know by now
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data): # if everything set
            try:
                login_user(user, remember=form.remember.data)
                #next_page = request.args.get('next') # the get method with () makes it optional, the square brackets will throw an error
                
                # so the below lines of code is mainly for the streak function, follow carefully, you'll get it. 
                login_time = datetime.now() # gets the log in time of the user
                last_login = user.user_streak[-1].last_login  # fetches last login from the database, the [-1] is to get the most recent, read on indexing tsw
         
                streak = fxns.streak_checker(login_time, last_login) # calls the function to see if streak is good, the function returns a list
                user.user_streak[-1].current_streak = streak[0] # this is current streak, the indexing is for the first item on the list
                user.user_streak[-1].longest_streak = streak[1] # longest streak
                user.user_streak[-1].last_login = login_time   # this makes the current login time replace the last login time
                user.user_streak[-1].streak_points += streak[2] # streak points, is added upon. see fxn module, you go barb
                db.session.commit()
                
                # the fourth item that the streak_checker function returns is a flag sort of. if it is equal to a certain number, certain alerts are called
                if streak[3] == 2:
                    flash("You Lost your streak! \n Use the site everyday to maintain it!", 'success')
                elif streak[3] == 1:
                    flash("Welcome Back", 'success')
                else:
                    flash("Congrats! You gained a point for maintaining you streak!", 'success')
                
                return redirect(url_for('users.haven'))  # turnary(google it) condition and change the redirect to accounts page
            except:
                login_user(user, remember=form.remember.data)
                return redirect(url_for('users.unconfirmed'))
        else:
            flash('Your email and password don\'t match! Please check and re-enter your details.', 'success')
            # if your email and password don't match this is your thing
    return render_template('Homepage.html', title = 'Home', form=form)

'''
Okay so for the home. We need something for the streak to be equated to since we are return statement is one.
Just leave it chale. lmao
'''




@main.route("/about")
def about():
    return render_template('about.html', title='About')

@main.route("/about-dev")
def about_dev():
    return render_template('about_dev.html', title = 'About - Developers')
 
'''
 You'll be seeing some flash(medhashe, something)
 It just sends a message to the web page for the user, it is a one time message, leaves after refresh
 
 It is a flask thing, 3y3 ah read on it okay? It is good. Read the flask documentation, it is good okay? Read o
 '''





