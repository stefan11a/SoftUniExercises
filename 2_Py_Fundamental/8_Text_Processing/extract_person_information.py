n = int(input())

for i in range(n):

    line = input()
    some_string = line.split()
    name = ''
    age = ''

    for word in some_string:
        if word[0] == '@':
            name = word.split('@')[1].split('|')[0]
        elif word[0] == '#':
            age = word.split('#')[1].split('*')[0]

    if name in line and age in line:
        print(f'{name} is {age} years old.')
