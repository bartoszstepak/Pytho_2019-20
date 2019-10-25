# print "\nTask 3.1"

# x = 2;
# y = 3;
# if (x > y):
#    result = x;
# else:
#    result = y;
# sredniki i nawiasy nie sa potrzebne

# for i in "qwerty": if ord(i) < 100: print i

# for i in "axby": print ord(i) if ord(i) < 100 else i

# print "\nTask 3.2"

# L = [3, 5, 4];
# srednik nie jest potrzebny
# L = L.sort()
# sort() nic nie zwraca - wystarczy napisac L.sort()

# x, y = 1, 2, 3
# nie mozna przypisac 3 wartosci do 2 zmiennych

# X = 1, 2, 3 ; X[1] = 4
# nie mozna nadpisywac wartosci w krotce

# X = [1, 2, 3] ; X[3] = 4
# X nie ma indeksu 3 - najwyzszy to 2

# X = "abc" ; X.append("d")
# nie ma funkcji append() dla stringow

# map(pow, range(8))
# pow przyjmuje conajmniej 2 argumenty

print "\nTask 3.3"

for i in range(31):
    if i % 3 != 0:
        print i

print "\nTask 3.4"

while True:
    inputNumber = raw_input("Podaj liczbe lub zakoncz program wpisujac stop \n")
    if inputNumber == "stop":
        break
    try:
        floatInput = float(inputNumber)
    except ValueError:
        print "Powinies podac liczbe!"
    print inputNumber
    print float(inputNumber) ** 3

print "\nTask 3.5"

print "Miarka"
size = int(raw_input("Podaj dlugosc miarki "))
line = ""

for i in range(size):
    line += "|...."

line += "|\n"
line += "0"

for i in range(size):
    line += "%5s" % (i + 1)

print line

print "\nTask 3.6"

height = int(raw_input("Podaj wysokosc ramki: "))
width = int(raw_input("Podaj szerokosc ramki: "))
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

print rect

print "\nTask 3.8"

list1 = [1, 3, 6, 12, 311, 223, 2, 5, 1]
list2 = [1, 6, 12, 222, 4, 5, 9]

# wystepujace w obu sekwencjach
print list(set(list1).intersection(list2))

# lista wszystkich z obu sekwencji
print list(set().union(list1, list2))

print "\nTask 3.9"

list1 = [[4], [], (4, 7), [1, 2, 3], (43, 1, 2, 7)]
result = []

for i in list1:
    result.append(sum(i))
print result

print "\nTask 3.10"

numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman2int(number):
    result_number = 0
    previous_value = None
    for letter in reversed(number):
        value = numerals[letter]
        if (previous_value is None) or (previous_value <= value):
            result_number += value
        else:
            result_number -= value
        previous_value = value

    return result_number


print roman2int("XXIV")
