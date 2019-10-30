def printTaskNumer(number):
    print("\nTask ", number)


printTaskNumer(4.2)


def get_line(size):
    line = ""

    for i in range(size):
        line += "|...."

    line += "|\n"
    line += "0"

    for i in range(size):
        line += "%5s" % (i + 1)

    return line


def get_rectangle(height, width):
    row = "+---"
    column = "|   "

    rect = ""
    for i in range(height):
        for x in range(width):
            rect += row
        rect += "+\n"
        for y in range(width):
            rect += column
        rect += "|\n"
    for z in range(width):
        rect += row
    rect += "+\n"

    return rect


print(get_line(4))
print(get_rectangle(3, 4))


printTaskNumer(4.3)


def factorial(n):
    x = 1
    for i in range(2, n + 1):
        x *= i
    return x


print(factorial(3))


printTaskNumer(4.4)


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        b += a
        a = b - a

    return b


print(fibonacci(5))


printTaskNumer(4.5)

# roziwązanie rekurencyjne jest mniej optymalne w tym wypadku niż interazyjne
# rozwiąznie iteracyjne

def odwracanie(List, left, right):
    if left >= 0 and right <= len(List):
        while left < right:
            tmp = List[left]
            List[left] = List[right]
            List[right] = tmp
            left += 1
            right -= 1

        return List
    else:
        return "niepoprawne indexy"


List = [1, 2, 3, 4, 5, 6]

print(List)
print(odwracanie(List, 0, 3))


printTaskNumer(4.6)


def sum_seq(sequence):

    sum = 0

    for element in sequence:
        if isinstance(element, (list, tuple)):
            sum += sum_seq(element)
        else:
            sum += element

    return sum


sequence = [1, 2, [1, 1], 5, (1, 1, 1)]

print(sum_seq(sequence))


printTaskNumer(4.7)


def flatten(sequence):

    flat_sequence = []

    for element in sequence:
        if isinstance(element, (list, tuple)):
            flat_sequence.extend(flatten(element))
        else:
            flat_sequence.append(element)

    return flat_sequence


sequence = [1, [1, [1, [2, (1, 1, [1, 1])]]]]

print(flatten(sequence))


