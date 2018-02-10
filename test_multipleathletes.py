import unittest
from MultipleAthletes import multipleathletes, athletelistfromform
from AthleteAnalysis import rankathletes


class AthleticsTestCase (unittest.TestCase):

    AthleteList = [{
        'fn': 'Sam',
        'ln': 'Brockway',
        'cl': 'Winchester'
    }, {
        'fn': 'Reiss',
        'ln': 'Jarvis',
        'cl': 'Southampton'
    }, {
        'fn': 'Freya',
        'ln': 'Coe',
        'cl': 'Southampton'
    }, {
        'fn': 'Sam',
        'ln': 'Jones',
        'cl': 'Southampton'
    }, {
        'fn': 'Harry',
        'ln': 'Richardson',
        'cl': 'Basingstoke'

    }]

    #@unittest.skip("skipping")
    def test_fetchathlete(self):
        #Test to make sure that each athlete has a result list.
        result = multipleathletes('400',self.AthleteList)
        self.assertEqual(len(result), len(self.AthleteList))


        #self.assertEqual('profile.aspx?athleteid=449292',result)
        #result = fetchathlete('Reiss','Jarvis','Southampton')
        #self.assertEqual('profile.aspx?athleteid=537630',result)

    def test_trackprediction(self):
        #Test to see if all track results get sorted into ascending order.
        Event = '400'
        Results = multipleathletes(Event, self.AthleteList)
        Prediction = rankathletes(self.AthleteList, Results, Event)
        self.assertEqual(len(Prediction), len(self.AthleteList))
        for x in range(0, len(self.AthleteList)-1):
            if Prediction[x+1]['rt'] > 0: #Athletes with no results are always sorted to be at the end.
                self.assertTrue(Prediction[x]['rt'] <= Prediction[x+1]['rt'], 'Track results in ascending order.')

    #@unittest.skip("skipping field event")
    def test_fieldprediction(self):
        #Test to see if all field results get sorted into descending order.
        Event = 'HJ'
        Results = multipleathletes(Event, self.AthleteList)
        Prediction = rankathletes(self.AthleteList, Results, Event)
        self.assertEqual(len(Prediction), len(self.AthleteList))
        for x in range(0, len(self.AthleteList)-1):
            self.assertTrue(Prediction[x]['rt'] >= Prediction[x+1]['rt'], 'Field results in descending order.')

    def test_athletelistfromforn(self):
        #Test to see if function can format the webpage inputs into lists of athletes.
        fn = ['Sam', 'Reiss', 'Freya', 'Sam', 'Harry']
        ln = ['Brockway', 'Jarvis', 'Coe', 'Jones', 'Richardson']
        cl = ['Winchester', 'Southampton', 'Southampton', 'Southampton', 'Basingstoke']
        Result = athletelistfromform(fn, ln, cl)
        self.assertEqual(Result, self.AthleteList)

    def test_invalidathlete(self):
        #Test to see if an invalid athlete is inputted.
        Event = 'HJ'
        UnknownAthlete = [{
            'fn': 'zzzz',
            'ln': 'zzzz',
            'cl': 'Wizzchester'
        }]
        Results = multipleathletes(Event, UnknownAthlete)
        Prediction = rankathletes(UnknownAthlete, Results, Event)
        self.assertEqual(len(Prediction), len(UnknownAthlete))
