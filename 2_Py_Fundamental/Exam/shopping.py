shopping_list = {}
item_list = []
important_item = []
is_important = False

while True:

    command = input().split('->')

    if command[0] == 'Go Shopping':
        break

    elif command[0] == 'Add':
        store = command[1]
        items = command[2].split(',')

        if store not in shopping_list.keys():
            shopping_list[store] = []
            for item in items:
                if item not in item_list:
                    item_list.append(item)
                    shopping_list[store] += [item]

        else:
            for item in items:
                if item not in item_list:
                    item_list.append(item)
                    shopping_list[store] += [item]

    elif command[0] == 'Important':
        store = command[1]
        item = command[2]

        if store in shopping_list.keys():
            if item not in item_list:
                item_list.append(item)
                important_item.append(item)
                if item not in shopping_list[store]:
                    shopping_list[store].insert(0, item)
        else:
            if item not in item_list:
                item_list.append(item)
                shopping_list[store] = [item]
                important_item.append(item)

    elif command[0] == 'Remove':
        store = command[1]
        if store in shopping_list.keys():
            for item in important_item:
                if item in shopping_list[store]:
                    is_important = True

            if not is_important:
                del shopping_list[store]


for store in shopping_list.keys():
    print(f"{store}:")
    for item in shopping_list[store]:
        print(f'- {item}')