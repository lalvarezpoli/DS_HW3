import math
import unittest

def check_positive_num(*args):
    for var_value in args:
        if not isinstance(var_value, (int, float)):
            raise TypeError("Variable must be an int or float")
        elif var_value <=0:
            raise ValueError("Variable must be higher than 0")

class PlaneFigure:
    def compute_perimeter(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def compute_surface(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius
        check_positive_num(radius)
    def compute_perimeter_circle(self):
        return 2 * math.pi * self.radius
    def compute_surface_circle(self):
        return math.pi * self.radius ** 2

class TestCircle(unittest.TestCase):

    def test_circle_perimeter(self):
        # Test the computation of the perimeter for the circle
        circle = Circle(5)  # Sample value for the radius
        self.assertAlmostEqual(circle.compute_perimeter(), 2 * math.pi * 5, places=5)  # Perimeter of a circle with radius 5

    def test_circle_surface(self):
        # Test the computation of the surface for the circle
        circle = Circle(5)  # Sample value for the radius
        self.assertAlmostEqual(circle.compute_surface(), math.pi * 5 ** 2, places=5)  # Surface of a circle with radius 5

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
        self.assertAlmostEqual(circle.compute_perimeter(), 2 * math.pi * (10**6), places=5)
        self.assertAlmostEqual(circle.compute_surface(), math.pi * (10**6) ** 2, places=5)

if __name__ == '__main__':
    unittest.main()
