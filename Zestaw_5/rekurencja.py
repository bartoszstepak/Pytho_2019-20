def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        b += a
        a = b - a

    return b
