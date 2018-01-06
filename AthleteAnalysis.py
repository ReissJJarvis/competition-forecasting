from EventUnits import isTimedEvent
from sklearn import datasets, linear_model
from datetime import date, datetime


def calculateaverage(results):
    runningtotal = 0
    for result in results:
        runningtotal = runningtotal + result['performance']
    if runningtotal == 0:
        return 0
    else:
        return round(runningtotal / len(results), 2)

def linearregression(results, pdate = date.today()):
    Data_X = []
    Data_Y = []
    if not results:
        return 0

    for n in range(0, len(results)):
        Data_X.append( [ results[n]['date'].toordinal() ] )
        Data_Y.append(results[n]['performance'])

    #Create linear regression object
    regr = linear_model.LinearRegression()
    #Train the model
    regr.fit(Data_X, Data_Y)
    #Return prediction
    return round(regr.predict(pdate.toordinal())[0], 2)

def ridgeregression(results, pdate = date.today()):
    Data_X = []
    Data_Y = []
    if not results:
        return 0

    for n in range(0, len(results)):
        Data_X.append( [ results[n]['date'].toordinal() ] )
        Data_Y.append(results[n]['performance'])

    #Create linear regression object
    regr = linear_model.Ridge (alpha = .5)
    #Train the model
    regr.fit(Data_X, Data_Y)
    #Return prediction
    return round(regr.predict(pdate.toordinal())[0], 2)

def lassoregression(results, pdate = date.today()):
    Data_X = []
    Data_Y = []
    if not results:
        return 0

    for n in range(0, len(results)):
        Data_X.append( [ results[n]['date'].toordinal() ] )
        Data_Y.append(results[n]['performance'])

    #Create linear regression object
    regr = linear_model.Lasso (alpha = 0.1)
    #Train the model
    regr.fit(Data_X, Data_Y)
    #Return prediction
    return round(regr.predict(pdate.toordinal())[0], 2)

def lassolarsregression(results, pdate = date.today()):
    Data_X = []
    Data_Y = []
    if not results:
        return 0

    for n in range(0, len(results)):
        Data_X.append( [ results[n]['date'].toordinal() ] )
        Data_Y.append(results[n]['performance'])

    #Create linear regression object
    regr = linear_model.LassoLars (alpha = 0.1)
    #Train the model
    regr.fit(Data_X, Data_Y)
    #Return prediction
    return round(regr.predict(pdate.toordinal())[0], 2)

def bayesianregression(results, pdate = date.today()):
    Data_X = []
    Data_Y = []
    if not results:
        return 0

    for n in range(0, len(results)):
        Data_X.append( [ results[n]['date'].toordinal() ] )
        Data_Y.append(results[n]['performance'])

    #Create linear regression object
    regr = linear_model.BayesianRidge()
    #Train the model
    regr.fit(Data_X, Data_Y)
    #Return prediction
    return round(regr.predict(pdate.toordinal())[0], 2)

def predictresult(results):
    #return calculateaverage(results)
    return linearregression(results)


    #Receive list of athletes, results and event
def rankathletes(athletes, results, event):
    Predictions = []

    #Calculate predicted Results for each athlete
    for n in range(0, len(athletes)):
        athletes[n]['rt'] = predictresult(results[n])

        #athletes[n].append({'rt' : predictresult(Results[n])})

        #print(athletes[n])
    #Sort in order of best to worst (track events lowest number to highest, field events highest to lowest)
    PredictedOutcome = sorted(athletes, key=lambda athlete : athlete['rt'], reverse = not isTimedEvent(event))
    #print position, name, and predicted performance
    #for n in range(0, len(athletes)):
    #    print(str(n+1), athletes[n])
    #return ordered list of position, athlete name, predicted performance
    return PredictedOutcome

    #def f(athletes, results, event):
    #    return ordered list of position, athlete name, predicted performance
