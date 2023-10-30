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

class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        check_positive_num(a, b)

    def compute_perimeter(self):
        return 2 * (self.a + self.b)

    def compute_surface(self):
        return self.a * self.b

class Test_Rectangle(unittest.TestCase):

    def test_rectangle_perimeter(self):
        # Test the computation of the perimeter for the rectangle
        rectangle = Rectangle(3, 4)  # Sample values for the sides
        self.assertEqual(rectangle.compute_perimeter(), 14)  # Perimeter of a rectangle with sides 3 and 4

    def test_rectangle_surface(self):
        # Test the computation of the surface for the rectangle
        rectangle = Rectangle(3, 4)  # Sample values for the sides
        self.assertEqual(rectangle.compute_surface(), 12)  # Surface of a rectangle with sides 3 and 4

    def test_negative_values(self):
        # Test instantiation with negative values
        with self.assertRaises(ValueError):
            Rectangle(3, -4)  # Negative value for b

    def test_non_numeric_values(self):
        # Test instantiation with non-numeric values
        with self.assertRaises(TypeError):
            Rectangle('a', 4)  # 'a' as value for a

    def test_zero_values(self):
        # Test instantiation with zero values
        with self.assertRaises(ValueError):
            Rectangle(0, 4)  # Zero value for a

    def test_large_values(self):
        # Test large values for sides
        rectangle = Rectangle(10**6, 10**6)
        # A very large rectangle; verify the calculated perimeter and surface
        self.assertEqual(rectangle.compute_perimeter(), 4 * (10**6))
        self.assertEqual(rectangle.compute_surface(), (10**6) * (10**6))

if __name__ == '__main__':
    unittest.main()
