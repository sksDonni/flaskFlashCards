from flask import render_template
from app import app
from app.forms import LoginForm
from app.forms import RegisterForm

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='flask flash cards!')

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='login', form=form)

@app.route('/register')
def register():
	form = RegisterForm()
	return render_template('register.html', title='register', form=form)

