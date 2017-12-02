import unittest
from AthleteLookup import fetchathlete
from MyAverage import fetchresults

class AthleticsTestCase (unittest.TestCase):
    def test_fetchathlete(self):
        result = fetchathlete('Freya','Coe','Southampton')
        self.assertEqual('profile.aspx?athleteid=449292',result)
        result = fetchathlete('Reiss','Jarvis','Southampton')
        self.assertEqual('profile.aspx?athleteid=537630',result)

    def test_fetchresults(self):
        athlete = fetchathlete('Freya','Coe','Southampton')
        self.assertEqual('profile.aspx?athleteid=449292',athlete)
        result = fetchresults('400',athlete)
        print(result)
        self.assertTrue(len(result) > 0)
        FirstRow = result[0]
        self.assertEqual(FirstRow['event'], '400')

# results = fetchathlete()
#print(results)
