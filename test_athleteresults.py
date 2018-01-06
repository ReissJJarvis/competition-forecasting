import unittest
from EventUnits import FormatResults
from AthletePerformances import fetchresults
from datetime import date, datetime, timedelta

class AthleteResultsTestCase (unittest.TestCase):
    def test_my800results(self):
        AthletePageID = 'profile.aspx?athleteid=537630'
        Event = '800'
        Results = fetchresults(Event, AthletePageID)
        self.assertIsInstance(Results, list)
        self.assertEqual(Results[0]['performance'], 127.1)
        self.assertEqual(Results[1]['performance'], 156.1)
        self.assertEqual(Results[2]['performance'], 125.9)
        self.assertEqual(Results[3]['performance'], 144)

    def test_my400results(self):
        AthletePageID = 'profile.aspx?athleteid=537630'
        Event = '400'
        Results = fetchresults(Event, AthletePageID)
        self.assertIsInstance(Results, list)
        self.assertEqual(Results[0]['performance'], 52.0)
        self.assertEqual(Results[1]['performance'], 52.1)
        self.assertEqual(Results[2]['performance'], 52.4)
        self.assertEqual(Results[3]['performance'], 52.8)

    def test_myljresults(self):
        AthletePageID = 'profile.aspx?athleteid=537630'
        Event = 'LJ'
        Results = fetchresults(Event, AthletePageID)
        self.assertIsInstance(Results, list)
        self.assertEqual(Results[0]['performance'], 4.4)
        self.assertEqual(Results[1]['performance'], 5.3)
        self.assertEqual(Results[2]['performance'], 4.68)

    def test_freya400results(self):
        AthletePageID = 'profile.aspx?athleteid=449292'
        Event = '400'
        Results = fetchresults(Event, AthletePageID)
        self.assertIsInstance(Results, list)
        self.assertEqual(Results[0]['performance'], 66.0)
        self.assertEqual(Results[1]['performance'], 66.1)
        self.assertEqual(Results[2]['performance'], 66.81)

    def test_lanaLJresults(self):
        AthletePageID = 'profile.aspx?athleteid=724147'
        Event = 'LJ'
        Results = fetchresults(Event, AthletePageID)
        self.assertIsInstance(Results, list)
        self.assertEqual(Results[0]['performance'], 5.09)
        self.assertEqual(Results[1]['performance'], 5.05)
        self.assertEqual(Results[2]['performance'], 4.98)

    def test_my400resultswithinyear(self):
        AthletePageID = 'profile.aspx?athleteid=537630'
        Event = '400'
        NoDays = 365
        Results = fetchresults(Event, AthletePageID, NoDays)
        #print('Results within a year:' , Results)
        self.assertIsInstance(Results, list)
        for x in range(0, len(Results)):
            self.assertTrue(Results[x]['date'] > date.today() - timedelta(days = NoDays))


        #Result = '56.28'
        #self.assertEqual(FormatResults(Result), 56.28, 'Time less than minute')
        #Result = '23.5'
        #elf.assertEqual(FormatResults(Result), 23.5, 'Distance')

#Define athlete page ID
#Call AthletePerformances lookup athlete results
#Inspect results to see if values correct
