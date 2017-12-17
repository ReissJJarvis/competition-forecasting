from EventUnits import isTimedEvent

def calculateaverage(results):
    runningtotal = 0
    for result in results:
        runningtotal = runningtotal + result['performance']
    if runningtotal == 0:
        return 0
    else:
        return round(runningtotal / len(results), 2)

def predictresult(results):
    return calculateaverage(results)

    #Receive list of athletes, results and event
def rankathletes(athletes, results, event):
    Predictions = []

    #Calculate predicted Results for each athlete
    for n in range(0, len(athletes)):
        athletes[n]['rt'] = round(predictresult(results[n]), 2)

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
