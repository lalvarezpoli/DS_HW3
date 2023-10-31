import math
import unittest
import hw4
from hw4 import check_positive_num, PlaneFigure,Circle


class TestCircle(unittest.TestCase):

    def test_circle_perimeter(self):
        # Test the computation of the perimeter for the circle
        circle = Circle(5)  # Sample value for the radius
        self.assertAlmostEqual(circle.compute_perimeter_circle(), 2 * math.pi * 5, places=5)  # Perimeter of a circle with radius 5

    def test_circle_surface(self):
        # Test the computation of the surface for the circle
        circle = Circle(5)  # Sample value for the radius
        self.assertAlmostEqual(circle.compute_surface_circle(), math.pi * 5 ** 2, places=5)  # Surface of a circle with radius 5

    def test_negative_value(self):
        # Test instantiation with a negative value
        with self.assertRaises(ValueError):
            Circle(-5)  # Negative value for radius

    def test_non_numeric_value(self):
        # Test instantiation with a non-numeric value
        with self.assertRaises(TypeError):
            Circle('a')  # 'a' as value for radius

    def test_zero_value(self):
        # Test instantiation with a zero value
        with self.assertRaises(ValueError):
            Circle(0)  # Zero value for radius

    def test_large_value(self):
        # Test large value for radius
        circle = Circle(10**6)
        # A very large circle; verify the calculated perimeter and surface
        self.assertAlmostEqual(circle.compute_perimeter_circle(), 2 * math.pi * (10**6), places=5)
        self.assertAlmostEqual(circle.compute_surface_circle(), math.pi * (10**6) ** 2, places=5)

if __name__ == '__main__':
    unittest.main()
