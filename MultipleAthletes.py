from AthleteLookup import fetchathlete
from AthletePerformances import fetchresults

def multipleathletes (Event, AthleteList, NoDays = -1):
    #Figure out how many people are in the lists
    #Send each person's fn, sn and club one at a time to AthleteLookup
    ListOfResults = []
    for Athlete in AthleteList:
        AthleteID = fetchathlete(Athlete['fn'], Athlete['ln'], Athlete['cl'])
        Results = fetchresults(Event, AthleteID, NoDays)
    #Compile all results
        ListOfResults.append(Results)
    #Return the results
    return ListOfResults

def athletelistfromform (fn, ln, cl):
    #Initialise empty AthleteList
    AthleteList = []

    #For each first name
    for x in range(0, len(fn)):

        #Create an athlete from fn, ln and cl if they are all populated
        if len(fn[x]) > 0 and len(ln[x]) > 0 and len(cl[x]) > 0:
            Athlete = {'fn' : fn[x] ,'ln' : ln[x],'cl' : cl[x]}

            #append athlete to AthleteList
            AthleteList.append(Athlete)

    #Return AthleteList
    return AthleteList
