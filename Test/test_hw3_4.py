from functools import reduce
import unittest

import hw3
from hw3 import sum_general_int_list


class test_sum_general_int_list(unittest.TestCase):

    def test_sum_general_int_list_standard(self):
        list_1 = [[2], 3, [[1, 2], 5]]
        result = sum_general_int_list(list_1)
        expected = 2 + 3 + (1 + 2) + 5
        assert result == expected

    def test_sum_general_int_list_single(self):
        list_3 = [7]
        result = sum_general_int_list(list_3)
        expected = 7
        assert result == expected

    def test_sum_general_int_list_empty_lists(self):
        list_4 = [[], [[]], [[], []]]
        result = sum_general_int_list(list_4)
        expected = 0
        assert result == expected

    def test_sum_general_int_list_nested(self):
        list_5 = [1, [2, [3, 4], 5], 6]
        result = sum_general_int_list(list_5)
        expected = 1 + 2 + (3 + 4) + 5 + 6
        assert result == expected


if __name__ == '__main__':
    unittest.main()
