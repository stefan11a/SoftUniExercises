def single_string(chr1, chr2):
    some_string = ''
    for i in range(chr1 + 1, chr2):
        some_string += chr(i) + ' '
    return some_string


char1 = ord(input())
char2 = ord(input())

print(single_string(char1, char2))
