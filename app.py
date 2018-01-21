from flask import Flask, render_template, request
from MultipleAthletes import multipleathletes, athletelistfromform
from AthleteAnalysis import rankathletes

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/forecast', methods=['GET', 'POST'])
def forecast():
    if request.method == 'POST':
        NoDays = 365*2.5
        event = request.form.get('event', '100')
        fn = request.form.getlist('fn[]')
        ln = request.form.getlist('ln[]')
        cl = request.form.getlist('cl[]')
        app.logger.debug('Form Event: %s FN: %s LN: %s CL: %s', event, fn, ln, cl)
        AthleteList = athletelistfromform(fn, ln, cl)
        Results = multipleathletes(event, AthleteList, NoDays)
        Forecast = rankathletes(AthleteList, Results, event)
        app.logger.debug('Forecast: %s', Forecast)
        #do_the_login()
        return render_template('results.html', Forecast=Forecast, athletes=len(Forecast), event=event)
    else:
        return render_template('forecastform.html', athletes=8)
