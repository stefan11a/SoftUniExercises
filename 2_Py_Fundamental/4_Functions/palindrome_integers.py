positive_integers = list(map(int, input().split(', ')))

for i in positive_integers:
    if i == int(str(i)[::-1]):
        print('True')
    else:
        print('False')
