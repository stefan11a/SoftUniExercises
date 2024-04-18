shopping_list = input().split('!')

while True:

    line = input()

    if line == 'Go Shopping!':
        print(', '.join(shopping_list))
        break

    command = line.split()

    if command[0] == 'Urgent':
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])
    elif command[0] == 'Unnecessary':
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
    elif command[0] == 'Correct':
        if command[1] in shopping_list:
            shopping_list = [sub.replace(command[1], command[2]) for sub in shopping_list]
    elif command[0] == 'Rearrange':
        if command[1] in shopping_list:
            shopping_list.remove(command[1])
            shopping_list.append(command[1])
