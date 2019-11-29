from fractions import gcd


class Frac:
    """Klasa reprezentujaca ulamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return "{0}".format(self.x)
        else:
            return "{0}/{1}".format(self.x, self.y)

    def __repr__(self):
        return "Frac({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        frac = Frac(self.x * other.y + self.y * other.x, self.y * other.y)
        return Frac(frac.x / gcd(frac.x, frac.y), frac.y / gcd(frac.x, frac.y))

    def __sub__(self, other):
        frac = Frac(self.x * other.y - self.y * other.x, self.y * other.y)
        return Frac(frac.x / gcd(frac.x, frac.y), frac.y / gcd(frac.x, frac.y))

    def __mul__(self, other):
        frac = Frac(self.x * other.x, self.y * other.y)
        return Frac(frac.x / gcd(frac.x, frac.y), frac.y / gcd(frac.x, frac.y))

    def __div__(self, other):
        frac = Frac(self.x * other.y, self.y * other.x)
        return Frac(frac.x / gcd(frac.x, frac.y), frac.y / gcd(frac.x, frac.y))

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def __cmp__(self, other):
        new_frac = self - other
        if new_frac.x == 0:
            return 0
        elif (new_frac.x > 0 and new_frac.y > 0) \
                or (new_frac.x < 0 and new_frac.y < 0):
            return 1
        else:
            return -1

    def __float__(self):
        return float(self.x) / float(self.y)

    def nwd(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
# Kod testujacy modul.

import unittest


class TestFrac(unittest.TestCase):

    def setUp(self): pass

    def test_str(self):
        self.assertEqual(str(Frac(1, 2)), "1/2")
        self.assertEqual(str(Frac(2, 1)), "2")

    def test_repr(self):
        self.assertEqual(repr(Frac(4, 5)), "Frac(4, 5)")
        self.assertEqual(repr(Frac(-2, 3)), "Frac(-2, 3)")

    def test_add(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))
        self.assertEqual(Frac(2, 4) + Frac(1, 6), Frac(2, 3))

    def test_sub(self):
        self.assertEqual(Frac(-12, 5) - Frac(3, 12), Frac(-53, 20))
        self.assertEqual(Frac(3, 5) - Frac(4, 16), Frac(7, 20))

    def test_mul(self):
        self.assertEqual(Frac(4, 3) * Frac(1, 7), Frac(4, 21))
        self.assertEqual(Frac(3, 5) * Frac(4, 16), Frac(3, 20))

    def test_div(self):
        self.assertEqual(Frac(2, 4) / Frac(1, 4), Frac(2, 1))
        self.assertEqual(Frac(7, 14) / Frac(9, 7), Frac(7, 18))

    def test_pos(self):
        self.assertEqual(+Frac(-1, 2), Frac(-1, 2))
        self.assertEqual(+Frac(2, -4), Frac(2, -4))
        self.assertEqual(+Frac(2, 4), Frac(2, 4))

    def test_neg(self):
        self.assertEqual(-Frac(-1, 2), Frac(1, 2))
        self.assertEqual(-Frac(2, -4), Frac(-2, -4))
        self.assertEqual(-Frac(2, 4), Frac(-2, 4))

    def test_invert(self):
        self.assertEqual(~Frac(-1, 2), Frac(2, -1))
        self.assertEqual(~Frac(2, -4), Frac(-4, 2))
        self.assertEqual(~Frac(2, 4), Frac(4, 2))

    def test_cmp_frac(self):
        self.assertEqual(cmp(Frac(3, 4), Frac(4, 5)), -1)
        self.assertEqual(cmp(Frac(2, 12), Frac(1, 6)), 0)
        self.assertEqual(cmp(Frac(4, 12), Frac(1, 6)), 1)

    def test_frac2float(self):
        self.assertEqual(float(Frac(3, 4)), 0.75)
        self.assertEqual(float(Frac(-1, 2)), -0.5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
