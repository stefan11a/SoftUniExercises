the_string = [char for char in input() if char != ' ']

dictionary = {}

for char in the_string:
    occurrences = the_string.count(char)
    dictionary[char] = occurrences

for letter in dictionary:
    print(f'{letter} -> {dictionary[letter]}')
