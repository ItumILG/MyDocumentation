import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    # площадь
    def test_area_normal(self):
        self.assertEqual(area(5, 10), 50)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 0), 0)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4.2), 10.5)

    def test_area_negative(self):
        # При написании 2 лабы я не продумывал, что произойдет при отрицательных значениях,
        # поэтому просто проверим алгебраическое значение
        self.assertEqual(area(-5, 10), -50)

    # периметр
    def test_perimeter_normal(self):
        self.assertEqual(perimeter(5, 10), 30)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 0), 0)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5), 12.0)

    def test_perimeter_negative(self):
        self.assertEqual(perimeter(-5, 10), 10)


if __name__ == "__main__":
    unittest.main()