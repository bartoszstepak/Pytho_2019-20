line = """Lorem Ipsum is simply dummy text of 
the printing and typesetting industry. 
Lorem Ipsum has been the industry's 
standard dummy text ever since the 1500s."""

print "\nTask 2.10"

print len(line.split())

print "\nTask 2.11"

word = "word"
word_letters = list(word)

new_word = "_".join(word_letters)

print new_word

print "\nTask 2.12"

print "\nWord built of first letters"
print "".join(map(lambda x: x[0], line.split()))

print "\nWord built of last letters"
print "".join(map(lambda x: x[len(x) - 1], line.split()))

print "\nTask 2.13"

print sum(map(lambda x: len(x), line.split()))

print "\nTask 2.14"

print "\nLongest word"
longest_word = max(line.split(), key=len)
print longest_word

print "\nLength of longest word"
print len(longest_word)

print "\nTask 2.15"

L = [1, 2, 3, 4, 5, 6]

word = "".join(str(x) for x in L)

print word

print "\nTask 2.16"

line = "example GvR text"
print line.replace("GvR", "Guido van Rossum")

print "\nTask 2.17"

print sorted(line.split())
print sorted(line.split(), key=len)

print "\nTask 2.18"

number = 1002300200304
print str(number).count("0")

print "\nTask 2.19"

L = [7, 23, 555, 41, 1, 345, 999, 22]

word = " ".join(map(lambda x: str(x).zfill(3), L))
print word
