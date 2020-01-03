from data_to_sort import *

print("\n11.1")

print get_random_values(10)
print get_random_almost_sorted_values(10)
print get_random_almost_sorted_values_reverse(10)
print get_random_gauss_values(15)
print get_random_values_with_repeat(25, 5)

print("\n11.3")


def insertsort(list_to_sort, left, right, cmpfunc=cmp):
    for i in range(left + 1, right + 1):
        for j in range(i, left, -1):
            if cmpfunc(list_to_sort[j - 1], list_to_sort[j]) > 0:
                swap(list_to_sort, j - 1, j)


def swap(l, one, two):
    temp = l[one]
    l[one] = l[two]
    l[two] = temp


import random

N = 10
a_list = range(N)
random.shuffle(a_list)

print a_list

insertsort(a_list, 0, N - 1, cmpfunc=lambda x, y: -cmp(x, y))

print a_list
