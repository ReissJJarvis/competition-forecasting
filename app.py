from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
