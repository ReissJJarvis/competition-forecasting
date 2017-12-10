TimedEvents = ['60', '100', '200', '300', '400', '100H', '110H', '400H', '800', '1500', '3000', '5000', '10000', '3000SC']
# TimedEventsMins = ['800', '1500', '3000', '5000', '10000', '3000SC']
def isTimedEvent (Event):
    if Event in TimedEvents:
        return True
    else:
        return False

#def FormatResults (Results, Event):
#    if isTimedEvent(Event):
#        for x in range (0, len(Results)):
#            if ':' in Results[x]:
#                Mins,Secs = Results[x].split('.')
#                Secs,MSecs = Secs.split(':')
#                print(Mins, ' min ', Secs, ' secs ', MSecs)
#                FormattedMins = int(Mins) * 60
#                FormattedTimeStr = FormattedMins + int(Secs)
#                FormattedTimeTogether = str(FormattedTimeStr) + '.'
#                FormattedTimeTogether = FormattedTimeTogether + MSecs
#                FormattedTime = float(FormattedTimeTogether)
#                Results[x] = FormattedTime
#    return(Results)

def FormatResults (Performance):
    if ':' in Performance:
        Mins,Secs = Performance.split(':')
        Secs,MSecs = Secs.split('.')
        #print(Mins, ' min ', Secs, ' secs ', MSecs)
        FormattedMins = int(Mins) * 60
        FormattedTimeStr = FormattedMins + int(Secs)
        FormattedTimeTogether = str(FormattedTimeStr) + '.'
        FormattedTimeTogether = FormattedTimeTogether + MSecs
        return(float(FormattedTimeTogether))
    else:
        return(float(Performance))
