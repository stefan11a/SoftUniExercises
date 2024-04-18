some_sequence = input().split()
some_string = input()

list_of_some_string = list(some_string)
message = []

for index in range(len(some_sequence)):
    index_as_int = int(some_sequence[index])
    index_as_list = list(map(int, str(index_as_int)))
    current_sum = sum(index_as_list)

    if current_sum < len(list_of_some_string):
        message.append(list_of_some_string[current_sum])
        list_of_some_string.pop(current_sum)
    else:
        message.append(list_of_some_string[current_sum - len(list_of_some_string)])
        list_of_some_string.pop(current_sum - len(list_of_some_string))

print(''.join(message))