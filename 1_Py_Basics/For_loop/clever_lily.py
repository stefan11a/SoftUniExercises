lily_age = int(input())
price_w = float(input())
price_t = int(input())

budget = 0
toys = 0
money_brother = 0

for year in range(1, lily_age + 1):
    if year % 2 == 0:
        budget += int(year / 2) * 10
        money_brother += 1
    else:
        toys += 1

money_toys = toys * price_t
saved_money = money_toys + budget - money_brother

diff_money = abs(saved_money - price_w)

if saved_money >= price_w:
    print(f'Yes! {diff_money:.2f}')
else:
    print(f'No! {diff_money:.2f}')