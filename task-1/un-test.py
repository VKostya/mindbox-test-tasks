import unittest
import math
from geometry import Circle, Triangle


class TestGeometryCalculator(unittest.TestCase):
    def test_circle_validation(self):
        with self.assertRaises(ValueError):
            circle = Circle(-5)

    def test_circle_area(self):
        circle = Circle(5)
        self.assertEqual(circle.get_area(), 25 * math.pi)

    def test_triangle_validation(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(3, 4, 50)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertEqual(triangle.get_area(), 6)

    def test_right_triangle_check(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())


if __name__ == "__main__":
    unittest.main()
