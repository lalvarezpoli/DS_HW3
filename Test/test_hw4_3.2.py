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


# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.


class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h
        check_positive_num(base, c1, c2, h)


    def compute_perimeter_triangle(self):
        return self.base + self.c1 + self.c2

    def compute_surface_triangle(self):
        return 0.5 * self.base * self.h
    

class test_Triangle(unittest.TestCase):

    def test_triangle_perimeter(self):
        # Test the computation of the perimeter for the triangle
        triangle = Triangle(3, 4, 5, 6)  # Sample values for the sides and height
        self.assertEqual(triangle.compute_perimeter(), 12)  # Perimeter of a triangle with sides 3, 4, and 5

    def test_triangle_surface(self):
        # Test the computation of the surface for the triangle
        triangle = Triangle(3, 4, 5, 6)  # Sample values for the sides and height
        self.assertEqual(triangle.compute_surface(), 9)  # Surface of a triangle with base 3 and height 6

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
        # A very large triangle; verify the calculated perimeter and surface
        self.assertEqual(triangle.compute_perimeter(), 3 * (10**6))
        self.assertEqual(triangle.compute_surface(), 0.5 * (10**6) * (10**6))

if __name__ == '__main__':
    unittest.main()