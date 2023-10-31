import unittest
import hw4
from hw4 import check_positive_num, PlaneFigure, Triangle

    

class test_Triangle(unittest.TestCase):

    def test_triangle_perimeter(self):
        # Test the computation of the perimeter for the triangle
        triangle = Triangle(3, 4, 5, 6)  # Sample values for the sides and height
        self.assertEqual(triangle.compute_perimeter_triangle(), 12)  # Perimeter of a triangle with sides 3, 4, and 5

    def test_triangle_surface(self):
        # Test the computation of the surface for the triangle
        triangle = Triangle(3, 4, 5, 6)  # Sample values for the sides and height
        self.assertEqual(triangle.compute_surface_triangle(), 9)  # Surface of a triangle with base 3 and height 6

    def test_negative_values(self):
        # Test instantiation with negative values
        with self.assertRaises(ValueError):
            Triangle(3, -4, 5, 6)  # Negative value for c1

    def test_non_numeric_values(self):
        # Test instantiation with non-numeric values
        with self.assertRaises(TypeError):
            Triangle('a', 4, 5, 6)  # 'a' as base value

    def test_zero_height(self):
        # Test instantiation with a zero height
        with self.assertRaises(ValueError):
            Triangle(3, 4, 5, 0)  # Zero height value

    def test_large_values(self):
        # Test large values for sides and height
        triangle = Triangle(10**6, 10**6, 10**6, 10**6)
        result_per = triangle.compute_perimeter_triangle()
        result_sur = triangle.compute_surface_triangle()
        # A very large triangle; verify the calculated perimeter and surface
        self.assertEqual(result_per, 3 * (10**6))
        self.assertEqual(result_sur, 0.5 * (10**6) * (10**6))

if __name__ == '__main__':
    unittest.main()