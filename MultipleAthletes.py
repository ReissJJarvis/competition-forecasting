from AthleteLookup import fetchathlete
from AthletePerformances import fetchresults

def multipleathletes (Event, AthleteList):
    #Figure out how many people are in the lists
    #Send each person's fn, sn and club one at a time to AthleteLookup
    ListOfResults = []
    for Athlete in AthleteList:
        AthleteID = fetchathlete(Athlete['fn'], Athlete['ln'], Athlete['cl'])
        Results = fetchresults(Event, AthleteID)
    #Compile all results
        ListOfResults.append(Results)
    #Return the results
    return ListOfResults
