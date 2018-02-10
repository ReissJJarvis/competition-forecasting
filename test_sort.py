import unittest
from MergeSort import ResultsSort

class SortingTestCase (unittest.TestCase):
    def test_sortlisttrack(self):
        Input  = [{'rt': 50.2}, {'rt': 0}, { 'rt': 55}, { 'rt': 0}, { 'rt': 23}, { 'rt': 45}, { 'rt': 64}, { 'rt': 50}, { 'rt': 0}]
        Result = [{ 'rt': 23}, { 'rt': 45}, { 'rt': 50}, { 'rt': 50.2}, { 'rt': 55}, { 'rt': 64}, { 'rt': 0}, { 'rt': 0}, { 'rt': 0}]
        Output = ResultsSort(Input, True)
        print(Input)
        print()
        print(Output)
        print()
        self.assertEqual(Output, Result)

    def test_sortlistfield(self):
        Input  = [{ 'rt': 50.2}, { 'rt': 0}, { 'rt': 55}, { 'rt': 0}, { 'rt': 23}, { 'rt': 45}, { 'rt': 64}, { 'rt': 50}, { 'rt': 0}]
        Result = [{ 'rt': 64}, { 'rt': 55}, { 'rt': 50.2}, { 'rt': 50}, { 'rt': 45}, { 'rt': 23}, { 'rt': 0}, { 'rt': 0}, { 'rt': 0}]
        Output = ResultsSort(Input, False)
        print(Input)
        print()
        print(Output)
        print()
        self.assertEqual(Output, Result)
