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
    

import unittest

class Test_PlaneFigure(unittest.TestCase):

    def test_compute_perimeter_not_implemented(self):
        # Test that calling compute_perimeter raises NotImplementedError
        figure = PlaneFigure()
        with self.assertRaises(NotImplementedError):
            figure.compute_perimeter()

    def test_compute_surface_not_implemented(self):
        # Test that calling compute_surface raises NotImplementedError
        figure = PlaneFigure()
        with self.assertRaises(NotImplementedError):
            figure.compute_surface()

    def test_compute_perimeter_and_surface_in_subclass(self):
        # Test if a subclass can compute perimeter and surface correctly
        class Square(PlaneFigure):
            def __init__(self, side_length):
                self.side_length = side_length

            def compute_perimeter(self):
                return 4 * self.side_length

            def compute_surface(self):
                return self.side_length ** 2

        square = Square(5)
        self.assertEqual(square.compute_perimeter(), 20)
        self.assertEqual(square.compute_surface(), 25)

    def test_missing_compute_perimeter_in_subclass(self):
        # Test that missing compute_perimeter in a subclass raises NotImplementedError
        class MissingPerimeter(PlaneFigure):
            def compute_surface(self):
                return 0

        missing_perimeter = MissingPerimeter()
        with self.assertRaises(NotImplementedError):
            missing_perimeter.compute_perimeter()

    def test_missing_compute_surface_in_subclass(self):
        # Test that missing compute_surface in a subclass raises NotImplementedError
        class MissingSurface(PlaneFigure):
            def compute_perimeter(self):
                return 0

        missing_surface = MissingSurface()
        with self.assertRaises(NotImplementedError):
            missing_surface.compute_surface()

if __name__ == '__main__':
    unittest.main()
