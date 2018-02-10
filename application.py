from flask import Flask, render_template, request
from MultipleAthletes import multipleathletes, athletelistfromform
from AthleteAnalysis import rankathletes

application = Flask(__name__)

@application.route('/') #Index page.
def index():
    return render_template('index.html') #Index page receives it's layout from index.html

@application.route('/forecast', methods=['GET', 'POST']) #Forecast page
def forecast():
    if request.method == 'POST':
        NoDays = 365*2.5
        event = request.form.get('event', '100')
        fn = request.form.getlist('fn[]')
        ln = request.form.getlist('ln[]')
        cl = request.form.getlist('cl[]')
        application.logger.debug('Form Event: %s FN: %s LN: %s CL: %s', event, fn, ln, cl)
        AthleteList = athletelistfromform(fn, ln, cl) #Formats inputs from page into the format needed.
        Results = multipleathletes(event, AthleteList, NoDays) #Gets the athletes' results
        Forecast = rankathletes(AthleteList, Results, event) #Uses the results to predict the next result
        application.logger.debug('Forecast: %s', Forecast)
        #do_the_login()
        return render_template('results.html', Forecast=Forecast, athletes=len(Forecast), event=event)
    else:
        return render_template('forecastform.html', athletes=8) #Forecast page receives it's layout from forecastform.html

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
