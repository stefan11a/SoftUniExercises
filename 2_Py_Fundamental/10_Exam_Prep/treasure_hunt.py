treasure = input().split('|')

line = input()

while not line == 'Yohoho!':

    command = line.split()

    if command[0] == 'Loot':
        for i in range(1, len(command)):
            item = command[i]
            if item not in treasure:
                treasure.insert(0, item)

    elif command[0] == 'Drop':
        index = int(command[1])
        if 0 < index < len(treasure):
            treasure.append(treasure[index])
            treasure.pop(index)

    elif command[0] == 'Steal':
        stolen_items = []
        count = int(command[1])
        if count >= len(treasure):
            for index in range(len(treasure) - 1, -1, -1):
                stolen_items.append(treasure[index])
                treasure.pop(index)
        else:
            final_index = len(treasure) - count - 1
            for index in range(len(treasure) - 1, final_index, -1):
                stolen_items.append(treasure[index])
                treasure.pop(index)
        print(', '.join(reversed(stolen_items)))

    line = input()

if len(treasure) == 0:
    print('Failed treasure hunt.')
else:
    average_gain = sum(len(item) for item in treasure) / len(treasure)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')
