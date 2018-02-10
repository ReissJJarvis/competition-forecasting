import unittest
from AthleteLookup import fetchathlete
from AthletePerformances import fetchresults

class AthleticsTestCase (unittest.TestCase):
    #See if the athlete page found is the same as the desired athlete page
    def test_fetchathlete(self):
        result = fetchathlete('Freya','Coe','Southampton')
        self.assertEqual('profile.aspx?athleteid=449292',result, 'Error on Freya')
        result = fetchathlete('Reiss','Jarvis','Southampton')
        self.assertEqual('profile.aspx?athleteid=537630',result, 'Error on Reiss')
        result = fetchathlete('Lynden','Olowe','Southampton')
        self.assertEqual('profile.aspx?athleteid=377028',result, 'Error on Lynden')
        result = fetchathlete('Jack','Higgins','Southampton')
        self.assertEqual('profile.aspx?athleteid=404176',result, 'Error on Jack')
        result = fetchathlete('Owen','Richardson','Basingstoke')
        self.assertEqual('profile.aspx?athleteid=119822',result, 'Error on Owen')


    def test_Lynden(self):
        #Input a user with a unique name
        result = fetchathlete('Lynden','Olowe','Southampton')
        self.assertEqual('profile.aspx?athleteid=377028',result, 'Error on Lynden')

    def test_sam(self):
        #Input a user without a unique name.
        athlete = fetchathlete('Sam','Jones','Southampton')
        self.assertEqual('profile.aspx?athleteid=538019',athlete)
        result = fetchresults('100',athlete)
        #print(result)
        self.assertTrue(len(result) > 0)
        FirstRow = result[0]
        self.assertEqual(FirstRow['event'], '100')

    def test_wrongclub(self):
        #Input a user with the incorrect club.
        athlete = fetchathlete('Reiss','Jarvis','Timbucktoo')
        self.assertIsNone(athlete)
        #result = fetchresults('100',athlete)
        ##print(result)
        #self.assertTrue(len(result) > 0)
        #FirstRow = result[0]
        #self.assertEqual(FirstRow['event'], '100')

    def test_fetchresults(self):
        #Test if the program can fetch the results.
        athlete = fetchathlete('Freya','Coe','Southampton')
        self.assertEqual('profile.aspx?athleteid=449292',athlete)
        result = fetchresults('400',athlete)
        #print(result)
        self.assertTrue(len(result) > 0)
        FirstRow = result[0]
        self.assertEqual(FirstRow['event'], '400')

# results = fetchathlete()
#print(results)
