from functools import reduce
from geopy.distance import geodesic as GD
import pandas as pd
from pandas.testing import assert_series_equal
import unittest

import hw3
from hw3 import compute_distance
  

class test_compute_distance(unittest.TestCase):

    def test_compute_distance_empty_input(self):
        coordinates = []
        result = compute_distance(coordinates)
        assert result == []

    def test_compute_distance_standard(self):    
        input_data=[((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
        result = compute_distance(input_data)
        expected = [GD(coord[0], coord[1]).km for coord in input_data]
        assert result == expected

    def test_compute_distance_single_coordinate(self):
        coordinates = [((41.23, 23.5), (41.5, 23.4))]
        result = compute_distance(coordinates)
        expected = [GD(coordinates[0][0], coordinates[0][1]).km]
        assert result == expected    

    def test_compute_distance_multiple_coordinates(self):
        coordinates = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8)), ((0.0, 0.0), (90.0, 180.0)), ((-90.0, -180.0), (90.0, 180.0))]
        result = compute_distance(coordinates)
        expected = [GD(coord[0], coord[1]).km for coord in coordinates]
        assert result == expected

if __name__ == '__main__':
    unittest.main()

