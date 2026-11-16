import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    # площадь
    def test_area_normal(self):
        self.assertEqual(area(10, 5), 25.0)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0.0)
        self.assertEqual(area(0, 5), 0.0)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4.2), 5.25)

    def test_area_negative(self):
        # Тоже закроем глаза на отрицательное значение
        self.assertEqual(area(-4, 5), -10.0)

    # периметр
    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(perimeter(6, 6, 6), 18)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(1.5, 2.5, 3.5), 7.5)

    def test_perimeter_invalid_triangle(self):
        #опустим неравенство треугольника
        self.assertEqual(perimeter(1, 2, 10), 13)


if __name__ == "__main__":
    unittest.main()