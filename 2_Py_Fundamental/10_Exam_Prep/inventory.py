journal = input().split(', ')


while True:

    command = input().split(' - ')

    if 'Craft!' in command:
        print(', '.join(journal))
        break

    if command[0] == 'Collect':
        item = command[1]
        if item not in journal:
            journal.append(item)
    elif command[0] == 'Drop':
        item = command[1]
        if item in journal:
            journal.remove(item)
    elif command[0] == 'Combine Items':
        item = command[1].split(':')
        old_item = item[0]
        new_item = item[1]
        if old_item in journal:
            for index in range(len(journal)):
                if old_item == journal[index]:
                    journal.insert(index + 1, new_item)
    elif command[0] == 'Renew':
        item = command[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)
