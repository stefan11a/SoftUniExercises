budget = float(input())
cards = int(input())
hard_disks = int(input())
RAM = int(input())

card_price = 250
hd_price = card_price * cards * 0.35
RAM_price = card_price * cards * 0.1

total_price = (cards * card_price) + (hard_disks * hd_price) + (RAM * RAM_price)

if cards > hard_disks:
    total_price = total_price - total_price * 0.15

if total_price > budget:
    print('Not enough money! You need ' + f'{(total_price - budget):.2f}' + ' leva more!')
else:
    print('You have ' + f'{(budget - total_price):.2f}' + ' leva left!')
