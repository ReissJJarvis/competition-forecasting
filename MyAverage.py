# 1. Extract results for event from powerOfTen
# 2. loop through results calculate running total
# 3. Calculate and print Average

import requests
from bs4 import BeautifulSoup
from datetime import date, datetime

def isresult(tag):
    if tag.name == "tr" and tag.contents[0].name == "td":
        return True
    else:
        return False

def isevent(tag, event):
    return tag.contents[0].contents[0] == event

def getresult(tag):
    result = {}
    result['event'] = tag.contents[0].string
    result['performance'] = float(tag.contents[1].string)
    result['wind'] = tag.contents[3].string
    result['position'] = tag.contents[5].string
    result['heat'] = tag.contents[6].string
    result['venue'] = tag.contents[9].string
    result['meeting'] = tag.contents[10].string
    result['date'] = datetime.strptime(tag.contents[11].string, "%d %b %y").date()
    return result

def fetchresults(event,athleteURL):
    poweroften = "http://www.thepowerof10.info/athletes/" + athleteURL
    page = requests.get(poweroften)
    #print (page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    performances = soup.find(id='cphBody_pnlPerformances')
    #print(type(performances))
    resultTags = performances.find_all(isresult)
    results = []
    for resultTag in resultTags:
        if isevent(resultTag, event):
            result = getresult(resultTag)
            results.append(result)
    return results

def calculateaverage(results):
    runningtotal = 0
    for result in results:
        runningtotal = runningtotal + result['performance']
    return runningtotal / len(results)

# event = input('Enter the event: ')
# poweroften = "http://www.thepowerof10.info/athletes/profile.aspx?athleteid=537630"
#results = fetchresults(event)
#print(results)


#average = calculateaverage(results)
#print(average)
#    if x.contents[0].name == "td":
#print(len(lists))
#print(lists)
