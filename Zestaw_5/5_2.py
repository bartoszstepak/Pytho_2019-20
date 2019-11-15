from fractions import gcd


def add_frac(frac1, frac2):
    return simplify_frac([frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1]])


def sub_frac(frac1, frac2):
    return simplify_frac([frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1]])


def mul_frac(frac1, frac2):
    return simplify_frac([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):
    if is_zero(frac2):
        return ZeroDivisionError
    return simplify_frac([frac1[0] * frac2[1], frac1[1] * frac2[0]])


def is_positive(frac):
    if (frac[0] > 0 and frac[1] > 0) \
            or (frac[0] < 0 and frac[1] < 0):
        return True
    else:
        return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False


def cmp_frac(frac1, frac2):
    y = sub_frac(frac1, frac2)
    if y[0] == 0:
        return 0
    elif is_positive(y):
        return 1
    else:
        return -1


def frac2float(frac):
    return float(frac[0]) / float(frac[1])


def simplify_frac(frac):
    new_frac = [frac[0] / gcd(frac[0], frac[1]), frac[1] / gcd(frac[0], frac[1])]
    return new_frac


f1 = [-1, 2]  # -1/2
f2 = [0, 1]  # zero
f3 = [3, 1]  # 3
f4 = [6, 2]  # 3 (niejednoznacznosc)
f5 = [0, 2]  # zero (niejednoznacznosc)

import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([2, 4], [1, 6]), [2, 3])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([-12, 5], [3, 12]), [-53, 20])
        self.assertEqual(sub_frac([3, 5], [4, 16]), [7, 20])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([4, 3], [1, 7]), [4, 21])
        self.assertEqual(mul_frac([3, 5], [4, 16]), [3, 20])

    def test_div_frac(self):
        self.assertEqual(div_frac([2, 4], [1, 4]), [2, 1])
        self.assertEqual(div_frac([7, 14], [9, 7]), [7, 18])

    def test_is_positive(self):
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([2, -4]), False)
        self.assertEqual(is_positive([2, 4]), True)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 3]), True)
        self.assertEqual(is_zero([4, 5]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([3, 4], [4, 5]), -1)
        self.assertEqual(cmp_frac([2, 12], [1, 6]), 0)
        self.assertEqual(cmp_frac([4, 12], [1, 6]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([3, 4]), 0.75)
        self.assertEqual(frac2float([-1, 2]), -0.5)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
