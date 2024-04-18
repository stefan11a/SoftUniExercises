dwarf_order = {}

while True:

    entry = input()

    if entry == "Once upon a time":
        break

    name, hat_color, power = entry.split(' <:> ')
    power = int(power)

    if hat_color not in dwarf_order.keys():
        dwarf_order[hat_color] = {}
    if name not in dwarf_order[hat_color]:
        dwarf_order[hat_color][name] = 0
        if power > dwarf_order[hat_color][name]:
            dwarf_order[hat_color][name] = power
    else:
        if power > dwarf_order[hat_color][name]:
            dwarf_order[hat_color][name] = power

sorted_hats = {}

for hat_color in dwarf_order.keys():
    for name, power in dwarf_order[hat_color].items():
        sorted_hats[hat_color] = name

for hat_color, dwarf in sorted_hats.items():
    for name, power in sorted(dwarf_order[hat_color].items(), key=lambda p: (-p[1], p[0])):
        print(f"({hat_color}) {dwarf} <-> {power}")
