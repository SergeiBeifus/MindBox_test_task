import unittest
from figures import Circle, Triangle


class TestFigures(unittest.TestCase):
    def test_circle(self):
        circle = Circle(radius=3.5)
        self.assertAlmostEqual(circle.radius, 3.5)
        self.assertAlmostEqual(circle.perimeter(), 2 * 3.5 * 3.141592653589793, places=5)
        self.assertAlmostEqual(circle.area(), 3.5 ** 2 * 3.141592653589793, places=5)

    def test_triangle(self):
        triangle = Triangle(side1=3.0, side2=4.0, side3=5.0)
        self.assertAlmostEqual(triangle.side1, 3.0)
        self.assertAlmostEqual(triangle.side2, 4.0)
        self.assertAlmostEqual(triangle.side3, 5.0)
        self.assertAlmostEqual(triangle.perimeter(), 12.0)
        self.assertAlmostEqual(triangle.area(), 6.0)
        self.assertTrue(triangle.is_orthogonal())

    def test_invalid_inputs(self):
        # Testing Circle with invalid inputs
        with self.assertRaises(TypeError):
            Circle(radius="3.5")
        with self.assertRaises(ValueError):
            Circle(radius=-3.5)

        # Testing Triangle with invalid inputs
        with self.assertRaises(TypeError):
            Triangle(side1="3")
        with self.assertRaises(ValueError):
            Triangle(side1=-3.0)
        with self.assertRaises(TypeError):
            Triangle(side2="4")
        with self.assertRaises(ValueError):
            Triangle(side2=-4.0)
        with self.assertRaises(TypeError):
            Triangle(side3="5")
        with self.assertRaises(ValueError):
            Triangle(side3=-5.0)
        with self.assertRaises(ValueError):
            Triangle(side1=1.0, side2=2.0, side3=10.0)  # Not a valid triangle


if __name__ == '__main__':
    unittest.main()
