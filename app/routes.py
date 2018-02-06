from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    #keep for templating purposes
    user = {'username' : 'Taylor'}
    posts = [
                {
                    'author' : {'username':'Jane'},
                    'body' : 'Derpty Der Der'
                }, 
                {
                    'author' : {'username':'John'},
                    'body' : 'Herp a Derp Derp'
                }
             ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    #return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, rememer_me{}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
