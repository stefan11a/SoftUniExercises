event = input()
coffee = 0

while event != 'END':

    if event == 'cat' or event == 'dog' or event == 'movie' or event == 'coding':
        coffee += 1
    elif event == 'CAT' or event == 'DOG' or event == 'MOVIE' or event == 'CODING':
        coffee += 2
    event = input()
    if coffee > 5:
        print('You need extra sleep')
        break
else:
    print(coffee)
