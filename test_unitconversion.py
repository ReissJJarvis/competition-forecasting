import unittest
from EventUnits import FormatResults

class UnitConversionTestCase (unittest.TestCase):
    def test_convertunits(self):
        Result = '1:56.28'
        self.assertEqual(FormatResults(Result), 116.28, 'Time over than a minute')
        Result = '56.28'
        self.assertEqual(FormatResults(Result), 56.28, 'Time less than minute')
        Result = '23.5'
        self.assertEqual(FormatResults(Result), 23.5, 'Distance')
