L = [4, 1, 2, 1, 6, 6, 1, 3, 1, 2, 4]

print("\n12.5")


def moda_py(L, left, right):
    dict_moda = {}
    item = left
    while item <= right:
        if L[item] in dict_moda:
            dict_moda[L[item]] += 1
        else:
            dict_moda[L[item]] = 1
        item += 1

    max_value = max(dict_moda.values())
    return [key for key, value in dict_moda.items() if value == max_value]


print("Array: {}".format(L))
print("Moda for items on indexes 3-6 {}".format(moda_py(L, 3, 6)))
print("Moda for items on indexes 0-10 {}".format(moda_py(L, 0, 10)))

print("\n12.6")


def lider_py(L, left, right):
    dict_moda = {}
    item = left
    while item <= right:
        if L[item] in dict_moda:
            dict_moda[L[item]] += 1
        else:
            dict_moda[L[item]] = 1
        item += 1

    max_value = max(dict_moda, key=dict_moda.get)
    if dict_moda[max_value] > (right + 1 - left) / 2:
        return max_value
    else:
        return None


print("Array: {}".format(L))
print("Lider for items on indexes 0-10(11 items): {}".format(lider_py(L, 0, 10)))
L = [4, 1, 4, 1, 4, 6, 1, 4, 4, 2, 4]
print("Array: {}".format(L))
print("Lider for items on indexes 0-10(11 items): {}".format(lider_py(L, 0, 10)))
print("Lider for items on indexes 7-10(4 items): {}".format(lider_py(L, 7, 10)))
