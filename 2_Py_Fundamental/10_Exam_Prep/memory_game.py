elements_sequence = input().split()
moves = 0

while True:

    line = input()

    if len(elements_sequence) == 0:
        print(f'You have won in {moves} turns!')
        break
    if line == 'end':
        print(f'Sorry you lose :(')
        print(' '.join(elements_sequence))
        break

    moves += 1

    current_indexes = line.split()
    index1 = int(current_indexes[0])
    index2 = int(current_indexes[1])

    if index1 == index2 or index1 > len(elements_sequence) or index1 < 0 or index2 > len(elements_sequence)\
            or index2 < 0:
        print(f'Invalid input! Adding additional elements to the board')
        middle_index = len(elements_sequence) // 2
        element_to_add = f'-{str(moves)}a'
        elements_sequence.insert(middle_index, element_to_add)
        elements_sequence.insert(middle_index + 1, element_to_add)
    else:
        element1 = elements_sequence[index1]
        element2 = elements_sequence[index2]
        if element1 == element2:
            print(f'Congrats! You have found matching elements - {element1}!')
            if index2 > index1:
                elements_sequence.remove(element2)
                elements_sequence.remove(element1)
            else:
                elements_sequence.remove(element1)
                elements_sequence.remove(element2)
        else:
            print('Try again!')

