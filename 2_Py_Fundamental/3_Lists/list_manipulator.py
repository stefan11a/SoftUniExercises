from sys import maxsize
some_list = input().split()
command_sequence = input().split()

command = command_sequence[0]
for i in range(0, len(some_list)):
    some_list[i] = int(some_list[i])

while command != 'end':

    if command == 'exchange':
        list_copy = some_list.copy()
        index = int(command_sequence[1])
        popped_list = []
        if index > len(list_copy) or index < 0:
            print('Invalid index')
        else:
            for j in range(len(list_copy) - 1, index, -1):
                popped_list.append(list_copy[j])
                list_copy.pop()
            popped_list.reverse()
            some_list = popped_list + list_copy

    elif command == 'max':
        max_even = -maxsize
        max_odd = -maxsize
        max_even_index = ''
        max_odd_index = ''
        for even_odd in range(len(some_list)):
            if some_list[even_odd] % 2 == 0 and some_list[even_odd] > max_even:
                max_even = some_list[even_odd]
            elif some_list[even_odd] % 2 != 0 and some_list[even_odd] > max_odd:
                max_odd = some_list[even_odd]
        if command_sequence[1] == 'even':
            for right_most_even in range(len(some_list) - 1, -1, -1):
                if some_list[right_most_even] == max_even:
                    max_even_index = right_most_even
                    break
            if max_even == -maxsize:
                print('No matches')
            else:
                print(max_even_index)
        elif command_sequence[1] == 'odd':
            for right_most_odd in range(len(some_list) - 1, -1, -1):
                if some_list[right_most_odd] == max_odd:
                    max_odd_index = right_most_odd
                    break
            if max_odd == -maxsize:
                print('No matches')
            else:
                print(max_odd_index)

    elif command == 'min':
        min_even = maxsize
        min_odd = maxsize
        min_even_index = ''
        min_odd_index = ''
        for even_odd in range(len(some_list)):
            if some_list[even_odd] % 2 == 0 and some_list[even_odd] < min_even:
                min_even = some_list[even_odd]
            elif some_list[even_odd] % 2 != 0 and some_list[even_odd] < min_odd:
                min_odd = some_list[even_odd]
        if command_sequence[1] == 'even':
            for right_most_even in range(len(some_list) - 1, -1, -1):
                if some_list[right_most_even] == min_even:
                    min_even_index = right_most_even
                    break
            if min_even == maxsize:
                print('No matches')
            else:
                print(min_even_index)
        elif command_sequence[1] == 'odd':
            for right_most_odd in range(len(some_list) - 1, -1, -1):
                if some_list[right_most_odd] == min_odd:
                    min_odd_index = right_most_odd
                    break
            if min_odd == maxsize:
                print('No matches')
            else:
                print(min_odd_index)

    elif command == 'first':
        even_list = []
        odd_list = []
        counter = int(command_sequence[1])
        if counter > len(some_list):
            print('Invalid count')
        else:
            for value in range(len(some_list)):
                if some_list[value] % 2 == 0:
                    even_list.append(some_list[value])
                else:
                    odd_list.append(some_list[value])
            if command_sequence[2] == 'even':
                for even_values in range(len(even_list) - 1, counter - 1, -1):
                    even_list.pop()
                print(even_list)
            if command_sequence[2] == 'odd':
                for odd_values in range(len(odd_list) - 1, counter - 1, -1):
                    odd_list.pop()
                print(odd_list)

    elif command == 'last':
        last_even_list = []
        last_odd_list = []
        counter = int(command_sequence[1])
        if counter > len(some_list):
            print('Invalid count')
        else:
            for value in range(len(some_list) - 1, -1, -1):
                if some_list[value] % 2 == 0:
                    last_even_list.append(some_list[value])
                else:
                    last_odd_list.append(some_list[value])
            if command_sequence[2] == 'even':
                for even_values in range(len(last_even_list) - 1, counter - 1, -1):
                    last_even_list.pop()
                last_even_list.reverse()
                print(last_even_list)
            if command_sequence[2] == 'odd':
                for odd_values in range(len(last_odd_list) - 1, counter - 1, -1):
                    last_odd_list.pop()
                last_odd_list.reverse()
                print(last_odd_list)

    command_sequence = input().split()
    command = command_sequence[0]

else:
    print(some_list)

