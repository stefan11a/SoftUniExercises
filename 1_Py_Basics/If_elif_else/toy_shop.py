excursion = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzle_price = puzzles * 2.60
dolls_price = dolls * 3
bears_price = bears * 4.10
minions_price = minions * 8.20
trucks_price = trucks * 2

total_price = puzzle_price + dolls_price + bears_price + minions_price + trucks_price
order = puzzles + dolls + bears + minions + trucks

if order >= 50:
    final_price = total_price * 0.75
else:
    final_price = total_price

winnings = final_price * 0.9
money_left = abs(winnings - excursion)

if winnings >= excursion:
    print(f'Yes! {money_left:.2f} lv left.')
else:

    print(f'Not enough money! {money_left:.2f} lv needed.')
