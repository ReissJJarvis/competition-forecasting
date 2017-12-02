import unittest
from MultipleAthletes import multipleathletes

class AthleticsTestCase (unittest.TestCase):
    def test_fetchathlete(self):
        NumberofAthletes = 8
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
        result = multipleathletes('400',AthleteList)
        print(result[0])
        print()
        print(result[1])
        print()
        print(result[2])
        print()
        print(result[3])
        print()
        print(result[4])
        self.assertEqual(len(result), 5)
        #self.assertEqual('profile.aspx?athleteid=449292',result)
        #result = fetchathlete('Reiss','Jarvis','Southampton')
        #self.assertEqual('profile.aspx?athleteid=537630',result)
