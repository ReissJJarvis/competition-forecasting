def calculateaverage(results):
    runningtotal = 0
    for result in results:
        runningtotal = runningtotal + result['performance']
    return runningtotal / len(results)

def predictresult(results):
    return calculateaverage(results)
