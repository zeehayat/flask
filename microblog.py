# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, flash, redirect
from config import Config
from app.forms import LoginForm
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from app import routes
# Flask constructor takes the name of 
# current module (__name__) as argument.
# app = Flask(__name__)


# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    user={'username': 'Zeeshan Hayat Azeemi'}
    posts=[
        {'author': {'name': 'Zeenux'},
         'body': {'Beautiful Day'}
         },
         {'author': {'name': 'ZuluKhan'},
         'body': {'Awesome Day'}
         }
         
    ]
    return render_template('index.html',title='Home',user=user, posts=posts)
@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user{}, remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',title='Sign in',form=form)
@app.route('/index')
# ‘/index’ URL is bound with index() function.
def index():
    return 'Index Page'
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()

