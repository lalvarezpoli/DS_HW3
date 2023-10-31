import unittest
import hw4
from hw4 import check_positive_num,PlaneFigure,Rectangle


class Test_Rectangle(unittest.TestCase):

    def test_rectangle_perimeter(self):
        # Test the computation of the perimeter for the rectangle
        rectangle = Rectangle(3, 4)  # Sample values for the sides
        self.assertEqual(rectangle.compute_perimeter_rectangle(), 14)  # Perimeter of a rectangle with sides 3 and 4

    def test_rectangle_surface(self):
        # Test the computation of the surface for the rectangle
        rectangle = Rectangle(3, 4)  # Sample values for the sides
        self.assertEqual(rectangle.compute_surface_rectangle(), 12)  # Surface of a rectangle with sides 3 and 4

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
        self.assertEqual(rectangle.compute_perimeter_rectangle(), 4 * (10**6))
        self.assertEqual(rectangle.compute_surface_rectangle(), (10**6) * (10**6))

if __name__ == '__main__':
    unittest.main()
