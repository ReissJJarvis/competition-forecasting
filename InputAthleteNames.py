from MultipleAthletes import multipleathletes
from AthleteAnalysis import rankathletes

#Input number of races and event
Event = input('Enter the event: ')
#Input number of people in one race
AthleteList = []
NumberOfAthletes = input('Enter the number of athletes: ')
#Input names and club of people in the one race
for x in range(0, int(NumberOfAthletes)):
    fn = input('Enter the first name of the athlete: ')
    ln = input('Enter the last name of the athlete: ')
    cl = input('Enter the club of the athlete: ')
    print()
    Athlete = {'fn' : fn ,'ln' : ln,'cl' : cl}
    AthleteList.append(Athlete)
#Call 'multipleathletes'
Results = multipleathletes(Event,AthleteList)
#print(Results[0])
print()
#print(Results[1])
#for each athlete call predict result
if int(NumberOfAthletes) != len(Results):
    print('THEY DONT MATCH.....')

#print a list of names and prediction
#Return the results
Prediction = rankathletes(AthleteList, Results, Event)
for p, r in enumerate(Prediction):
    print(p+1, r['fn'], r['ln'], r['rt'])
