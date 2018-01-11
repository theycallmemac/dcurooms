import unittest
import sys
import requests
sys.path.append('.')
from scripts.checks import search_dictionary
from scripts.builders import build_timetable
class SearchDictTestCase(unittest.TestCase):

    def test_not_in_dict_search(self):
        test_input_one = '0700'
        times = {
            '0800': '1',
            '0830': '2',
            '0900': '3',
            '0930': '4',
            '1000': '5',
            '1030': '6',
            '1100': '7',
            '1130': '8',
            '1200': '9',
            '1230': '10',
            '1300': '11',
            '1330': '12',
            '1400': '13',
            '1430': '14',
            '1500': '15',
            '1530': '16',
            '1600': '17',
            '1630': '18',
            '1700': '19',
            '1730': '20',
            '1800': '21',
            '1830': '22',
            '1900': '23',
            '1930': '24',
            '2000': '25',
            '2030': '26',
            '2100': '27',
            '2130': '28',
            '2200': '29',
            '2230': '30'}
        try:
            not_in_dict_result = search_dictionary(times, test_input_one)

        except SystemExit:
            pass

    def test_in_dict_search(self):
        test_input_two = '1600'
        times = {
            '0800': '1',
            '0830': '2',
            '0900': '3',
            '0930': '4',
            '1000': '5',
            '1030': '6',
            '1100': '7',
            '1130': '8',
            '1200': '9',
            '1230': '10',
            '1300': '11',
            '1330': '12',
            '1400': '13',
            '1430': '14',
            '1500': '15',
            '1530': '16',
            '1600': '17',
            '1630': '18',
            '1700': '19',
            '1730': '20',
            '1800': '21',
            '1830': '22',
            '1900': '23',
            '1930': '24',
            '2000': '25',
            '2030': '26',
            '2100': '27',
            '2130': '28',
            '2200': '29',
            '2230': '30'}
        in_dict_result = search_dictionary(times, test_input_two)
        self.assertTrue(int(in_dict_result) in range(1,31))


if __name__ == '__main__':
    unittest.main()

