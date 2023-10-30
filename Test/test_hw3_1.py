#### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

from functools import reduce

simba=["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

def count_simba(list_of_strings: list):
    return reduce(lambda x,y: x+y, map(lambda x: x.count("Simba"), list_of_strings))

count_simba(simba)


import pandas as pd
from pandas.testing import assert_series_equal
import unittest

class test_count_simba(unittest.TestCase):
    def test_count_simba_3occurrence():
    input_data = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
    result = count_simba(input_data)
    expected = 3
    assert result == expected

    def test_count_simba_single_occurrence():
    input_data = [["simba"]]
    result = count_simba(input_data)
    expected = 0
    assert result == expected

    def test_count_simba_empty_strings():
    input_data = ["", "", ""]
    result = count_simba(input_data)
    expected = 0
    assert result == expected

    def test_count_simba_mixed_cases():
    input_data = ["Simba and simba", "SIMBA is the Lion King", "Simba, SIMBA, and SiMba"]
    result = count_simba(input_data)
    expected = 9
    assert result == expected

    def test_count_simba_large_input():
    input_data = ["Simba and Nala are lions."] * 10**4  # A list with the string by 10k times
    result = count_simba(input_data)
    expected = 10**4
    assert result == expected

