print(8.1)

def solve1(a, b, c):
    if a == 0 and b == 0:
        if c == 0:
            print("nieokreslone")
        else:
            print("sprzeczne")
    elif a == 0 and c == 0:
        print("Rozwiazaniem jest y = 0")
    elif a == 0:
        print("Rozwiazaniem jest y = " + repr(float(c) / float(b)))
    elif b == 0:
        print("nieokreslone")
    elif c == 0:
        print("Rownanie postaci: \ny = ({0} * x)/{1}".format(a, b))
    else:
        print("Rownanie postaci: \ny = -({0} * x + {1})/{2}".format(a, c, b))

solve1(1, 3, 5)
solve1(0, 0, 0)
solve1(0, 0, 5)
solve1(0, 4, 0)
solve1(0, 3, 5)
solve1(1, 0, 7)
solve1(2, 3, 0)



print("8.3")
import random


def calc_pi(n=100):
    isOk = 0
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        if x * x + y * y <= 1:
            isOk = isOk + 1

    return float(4 * isOk) / n


print("PI: ")
print(calc_pi(134334))


print("8.4")

def isTriangle(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True


def heron(a, b, c):
    if isTriangle(a, b, c):
        return (((a + b + c) * (a + b - c) * (a - b + c) * (b + c - a)) ** 0.5) / 4
    else:
        raise ValueError("cannot create triangle")


print("Pole  trojkata: 1, 1, 1: ")
print(heron(1, 1, 1))


print("8.6")

def rek_P(i, j):
    if i == 0 and j == 0:
        return 0.5
    if i > 0 and j == 0:
        return 0
    if i == 0 and j > 0:
        return 1
    if j > 0 and i > 0:
        return 0.5 * (rek_P(i - 1, j) + rek_P(i, j - 1))


def dyn_P(x, y):
    maximum = max(x, y)
    P = {(0, 0): 0.5}

    for i in range(maximum + 1):
        P[(i, 0)] = 0
        P[(0, i)] = 1

    for i in range(1, maximum + 1):
        for j in range(1, maximum + 1):
            wartosc = 0.5 * (P[(i - 1, j)] + P[(i, j - 1)])
            P[(i, j)] = wartosc
    return P[(x, y)]


print("Rekurencyjnie: ")
print(rek_P(3, 4))
print("Dynamicznie: ")
print(dyn_P(3, 4))
