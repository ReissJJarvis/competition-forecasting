from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hi')
def hi():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    if request.method == 'POST':
        app.logger.debug('request.form.event %s', request.form.get('event'))
        app.logger.debug('request.form.fn %s', request.form.getlist('fn[]'))
        app.logger.debug('request.form.ln %s', request.form.getlist('ln[]'))
        app.logger.debug('request.form.cl %s', request.form.getlist('cl[]'))
        #do_the_login()
        return render_template('results.html', athletes=8)
    else:
        return render_template('forecastform.html', athletes=8)
