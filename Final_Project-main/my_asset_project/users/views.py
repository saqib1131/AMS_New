from flask import render_template, url_for, request, redirect, Blueprint, flash, session
from flask_login import login_user, logout_user
from my_asset_project import db, app
from my_asset_project.models import User
from my_asset_project.users.forms import RegistrationForm, LoginForm
import pdb
import json
from functools import wraps
import logging
from logging.handlers import RotatingFileHandler
from flask import jsonify
from werkzeug.security import check_password_hash


# def superuser_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if session.get('role') == 'Super':
#             return f(*args, **kwargs)
#         else:
#             # Handle unauthorized access here, such as redirecting or rendering an error page
#             print("No Access")
#             # return render_template('/unauthorized.html')
#     return decorated_function

users = Blueprint('users', __name__)

#register
@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
   
    if form.validate_on_submit():
        
        user = User(AIC_office = form.AIC_office.data,
                    user_email = form.user_email.data,
                    password= form.password.data)
        db.session.add(user)
        db.session.commit()
        #flash('Thanks for Registration!')
        #app.logger.info('New user added: %s by %s', form.user_email.data, session.get('name'))

        return redirect(url_for('users.login'))
    
    return render_template('add-user.html', form = form)

 #Import the 'flash' function from Flask
from flask import render_template, flash, redirect, url_for, request, flash

 # Your existing login route
@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    success_modal = False
    print(form.user_email.data, form.password.data, "1234")
    print("Form submitted:", request.method)
    print("Form validated:", form.validate_on_submit())
    print("Form errors:", form.errors)

    #-----------
    if request.method=='POST' and form.validate():
        user = User.query.filter_by(user_email = form.user_email.data).first()
        print(user.password_hash)
        if user:
            print("Yes")
            session['name'] = user.domain_name
            session['location']=user.AIC_office
            success_modal = True
            # Flash the message for use with templates
            #flash('Log in Success!')

            # Display an alert using JavaScript
        
            next = request.args.get('next')
            print(next, 'next')
            if next == None or not next[0]=='/':
                next = url_for('core.index')
            return redirect(next)
        else:
            flash("Email ID or Password is Incorrect!", "info")
            return render_template('login.html', form=form,success_modal=success_modal)     
              
    return render_template('login.html', form=form, success_modal=success_modal)

    # return render_template('login.html', form=form,success_modal=success_modal)

    #-----------
#     if form.validate_on_submit():
#          user = User.query.filter_by(user_email = form.user_email.data).first()
#          if user is not None and user.check_password(form.password.data):
#              session['role'] = user.role
#              session['name'] = user.domain_name
#              session['permissions']=user.Permissions
#              session['dept']=user.department
#              session['location']=user.AIC_office
#              success_modal = True
#              # Flash the message for use with templates
#              #flash('Log in Success!')

#              # Display an alert using JavaScript
            
#              next = request.args.get('next')

#              if next == None or not next[0]=='/':
#                  next = url_for('core.index')
#              return redirect(next)
#          else:
#             flash("Email ID or Password is Incorrect!", "info")
#             return render_template('login.html', form=form,success_modal=success_modal)

              
              
# #             return render_template('login.html', form=form, success_modal=success_modal)

#     return render_template('login.html', form=form,success_modal=success_modal)


@users.route("/add-user", methods=['GET', 'POST'])
def add_user():
    form = RegistrationForm()
    existing_user=""
    form.set_choices()
    print(form, "form")
    if session.get('role')=="Admin":
        form.set_department_choices()
    if form.validate_on_submit():
        print (form.domain_name.data)
        existing_user = User.query.filter_by(user_email=form.user_email.data).first()
        if existing_user:
                    flash('Email already exists. Please use a different email.', "info")
        else:
            if existing_user:
                flash('Email already exists. Please use a different email.', "info")
            else:
                user = User(AIC_office = form.AIC_office.data,
                            department = form.department.data,
                            role = form.role.data,
                            user_email = form.user_email.data,
                            domain_name= form.domain_name.data,
                            password= form.password.data,
                            )
            
            #db.drop_all()
            #db.create_all()
            db.session.add(user)
            db.session.commit()
            flash('User Added Successfully!', "info")
            print("Reached the logging statement")  
            app.logger.info('New user added: %s by %s', form.user_email.data, session.get('name'))

            #flash('Thanks for Registration!')
    return render_template('add-user.html', form = form)


#logout
@users.route("/logout")
def logout():
    session.pop('name', None)
    session.pop('role', None)
    session.pop('dept', None)

    logout_user()
    return redirect(url_for("users.login"))

 

@users.route("/get-user", methods=['GET'])
def get_user():
    user = User.query.all()
    r = [u.user_email for u in user]
    print("users",)


