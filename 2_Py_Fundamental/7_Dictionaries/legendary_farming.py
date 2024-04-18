runes = {"shards": 0, "fragments": 0, "motes": 0}

collected_items = input().split()
obtained = False
while not obtained:

    for index in range(0, len(collected_items), 2):
        material_quantity = int(collected_items[index])
        material_type = collected_items[index + 1].lower()

        if material_type not in runes.keys():
            runes[material_type] = 0
        runes[material_type] += material_quantity

        if runes["shards"] >= 250:
            legendary_item = 'Shadowmourne'
            runes["shards"] -= 250
            obtained = True
        elif runes["fragments"] >= 250:
            legendary_item = 'Valanyr'
            runes["fragments"] -= 250
            obtained = True
        elif runes["motes"] >= 250:
            legendary_item = 'Dragonwrath'
            runes["motes"] -= 250
            obtained = True
        if obtained:
            break
    if obtained:
        break

    collected_items = input().split()
print(f'{legendary_item} obtained!')

for material, quantity in runes.items():
    print(f'{material}: {quantity}')
