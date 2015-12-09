from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

# index view function suppressed for brevity

@app.route('/')
@app.route('/index')
@app.route('/login', methods=['GET','POST'])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login request for OpenID="{%s}", remember_me={%s}'
                .format(form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

def index():
    user = {'nickname': 'Miguel'} # fake user
    posts = [ #fake array of fake post from fake user
            {
                'author':{'nickname':'John'},
                'body':'Beautiful day in Portland!'
            },
            {
                'author':{'nickname':'Susan'},
                'body' : 'The Avengers movie was so cool!'
                }
            ]
    return render_template('index.html',
                            user=user,
                            posts=posts)

