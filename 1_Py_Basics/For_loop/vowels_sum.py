word = input()
number = 0

for i in word:
    if i == 'a':
        number += 1
    elif i == 'e':
        number += 2
    elif i == 'i':
        number += 3
    elif i == 'o':
        number += 4
    elif i == 'u':
        number += 5

print(number)