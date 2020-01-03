import random


def get_random_values(n):
    new_list = range(n)
    random.shuffle(new_list)
    return new_list


def swap(l, one, two):
    temp = l[one]
    l[one] = l[two]
    l[two] = temp


def get_random_almost_sorted_values(n):
    new_list = range(n)
    for i in range(0, n - 1, 2):
        swap(new_list, i, i + 1)
    return new_list


def get_random_almost_sorted_values_reverse(n):
    new_list = list(reversed(range(n)))
    for i in range(0, n - 1, 2):
        swap(new_list, i, i + 1)
    return new_list


def get_random_gauss_values(n):
    new_list = []
    for x in range(n):
        new_list.append(random.gauss(0.5, 0.2))
    random.shuffle(new_list)
    return new_list


def get_random_values_with_repeat(n, k):
    new_list = []
    how_to_left = n - k
    what_number = 0
    for i in range(n):
        is_good = random.randint(0, 1)
        if how_to_left > 0 and is_good == 1:
            how_to_left = how_to_left - 1
        else:
            if what_number < k:
                what_number = what_number + 1
        new_list.append(what_number)
    random.shuffle(new_list)
    return new_list
