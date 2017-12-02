from MultipleAthletes import multipleathletes
from AthleteAnalysis import predictresult

#Input number of races
Event = input('Enter the event: ')
#Input number of people in one race
AthleteList = []
NumberOfAthletes = input('Enter the number of athletes: ')
for x in range(0, int(NumberOfAthletes)):
    fn = input('Enter the first name of the athlete: ')
    ln = input('Enter the last name of the athlete: ')
    cl = input('Enter the club of the athlete: ')
    print()
    Athlete = {'fn' : fn ,'ln' : ln,'cl' : cl}
    AthleteList.append(Athlete)
#Input names and club of people in the one race
#Call 'multipleathletes'
results = multipleathletes(Event,AthleteList)
print(results[0])
print()
print(results[1])
#for each athlete call predict result
if int(NumberOfAthletes) != len(results):
    print('THEY DONT MATCH.....')

for n in range(0, int(NumberOfAthletes)):
    prediction = predictresult(results[n])
    print(AthleteList[n]['fn'] + ' ' + str(round(prediction,2)))
#print a list of names and prediction
#Return the results
