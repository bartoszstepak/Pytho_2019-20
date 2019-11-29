import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


# Kod testujacy modul.

import unittest


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.point1 = Point(2, 1)
        self.point2 = Point(0, 0)
        self.point3 = Point(3, 4)
        self.point4 = Point(0, 0)

    def test_str(self):
        self.assertEqual(str(self.point1), "(2, 1)")
        self.assertEqual(str(self.point2), "(0, 0)")

    def test_repr(self):
        self.assertEqual(repr(self.point3), "Point(3, 4)")
        self.assertEqual(repr(self.point4), "Point(0, 0)")

    def test_eq(self):
        self.assertEqual(self.point1 == self.point2, False)
        self.assertEqual(self.point2 == self.point4, True)

    def test_ne(self):
        self.assertEqual(self.point1 != self.point2, True)
        self.assertEqual(self.point2 != self.point4, False)

    def test_add(self):
        self.assertEqual(self.point1 + self.point3, Point(5, 5))
        self.assertEqual(self.point2 + self.point4, Point(0, 0))
        self.assertEqual(self.point1 + self.point4, Point(2, 1))

    def test_sub(self):
        self.assertEqual(self.point1 - self.point2, Point(2, 1))
        self.assertEqual(self.point1 - self.point3, Point(-1, -3))
        self.assertEqual(self.point3 - self.point1, Point(1, 3))

    def test_mul(self):
        self.assertEqual(self.point1 * self.point2, 0)
        self.assertEqual(self.point1 * self.point3, 10)

    def test_cross(self):
        self.assertEqual(self.point1.cross(self.point3), 5)
        self.assertEqual(self.point1.cross(self.point2), 0)
        self.assertEqual(self.point3.cross(self.point1), -5)

    def test_length(self):
        self.assertEqual(self.point2.length(), 0)
        self.assertEqual(self.point3.length(), 5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
