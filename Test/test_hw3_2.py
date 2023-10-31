import datetime
import pandas as pd
from pandas.testing import assert_series_equal
import unittest
import pytest

# Import function
import hw3 
from hw3 import get_day_month_year

#def get_day_month_year(list_of_dates: list):
    #return pd.DataFrame(map(lambda x: {"day": x.day, "month": x.month, "year": x.year}, list_of_dates))

#Me da error el data frame, no se cómo testearlo. Dice que es ambiguo y 'expected' not defined.

class test_get_day_month_year(unittest.TestCase):

    def test_get_day_month_year_standard(self):
        input_data = [datetime.date(2001, 1, 1), datetime.date(2032, 1, 2), datetime.date(2019, 1, 3), datetime.date(2019, 1, 4), datetime.date(2019, 1, 5), datetime.date(2019, 1, 6), datetime.date(2019, 1, 7), datetime.date(2019, 1, 8), datetime.date(2019, 1, 9), datetime.date(2019, 1, 10)]
        result = get_day_month_year(input_data)
        expected_dict = {"day": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "month": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], "year": [2001, 2032, 2019, 2019, 2019, 2019, 2019, 2019, 2019, 2019]}
        expected = pd.DataFrame(expected_dict)
        pd.testing.assert_frame_equal(result,expected)

        #assert result == expected
        #self.assertEquals(True,result.equals(expected))
    

    def test_get_day_month_year_empty(self):
        input_data = []
        result = get_day_month_year(input_data)
        expected_df = pd.DataFrame(columns=["day", "month", "year"])
        #assert result == expected_df
        pd.testing.assert_frame_equal(result,expected_df)


    def test_get_day_month_year_single_date(self):
        input_data = [datetime.date(2022, 12, 31)]
        result = get_day_month_year(input_data)
        expected_dict = {"day": [31], "month": [12], "year": [2022]}
        expected = pd.DataFrame(expected_dict)
        pd.testing.assert_frame_equal(result,expected)
        #assert result == expected

    def test_get_day_month_year_mixed_dates(self):
        input_data = [datetime.date(2001, 1, 1), datetime.date(2022, 5, 15), datetime.date(2033, 12, 31)]
        result = get_day_month_year(input_data)
        expected_dict = {"day": [1, 15, 31], "month": [1, 5, 12], "year": [2001, 2022, 2033]}
        expected_df = pd.DataFrame(expected_dict)
        #assert result == expected_df
        pd.testing.assert_frame_equal(result,expected_df)

    def test_get_day_month_year_repeated(self):
        input_data = [datetime.date(2022, 5, 15), datetime.date(2022, 5, 15)]
        result = get_day_month_year(input_data)
        expected_dict = {"day": [15], "month": [5], "year": [2022]}
        expected_df = pd.DataFrame(expected_dict)
        #assert result == expected_df
        pd.testing.assert_frame_equal(result,expected_df)
    

if __name__ == '__main__':
    unittest.main()
