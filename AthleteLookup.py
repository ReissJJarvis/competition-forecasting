# 1. Extract results for event from powerOfTen
# 2. loop through results calculate running total
# 3. Calculate and print Average

import requests
from bs4 import BeautifulSoup

poweroften = "http://thepowerof10.info/athletes/athleteslookup.aspx"

def fetchathlete(FirstName,SurName,Club):
    page1 = requests.get(poweroften)
    soup1 = BeautifulSoup(page1.text, 'html.parser')
    vstate = soup1.find(id='__VIEWSTATE')['value']
    eventvali = soup1.find(id='__EVENTVALIDATION')['value']
    payload = {'__VIEWSTATE': vstate,
    '__EVENTVALIDATION': eventvali,
    'ctl00$cphBody$txtSurname': SurName,
    'ctl00$cphBody$txtFirstName': FirstName,
    'ctl00$cphBody$ctl00$cphBody$txtClub': Club,
    'ctl00$cphBody$btnLookup': 'Lookup'}
    #print(payload)
    page2 = requests.post(poweroften, data=payload)
    #print(page2.status_code)
    soup2 = BeautifulSoup(page2.text, 'html.parser')
    searchresults = soup2.find(id='cphBody_dgAthletes') #ID in table of results
    #print(searchresults)
    if searchresults is None:
        athletepage = None
    else:
        athletepage = searchresults.find_all('tr')[1].contents[8].a['href']
    #print(type(performances))
    #resultTags = performances.find_all(isresult)
    #results = []
    #for resultTag in resultTags:
    #    if isevent(resultTag, event):
    #        result = getresult(resultTag)
    #        results.append(result)
    return athletepage
