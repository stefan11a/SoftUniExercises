film_budget = float(input())
extras = int(input())
price_clothes_extra = float(input())

price_clothes_extras = extras * price_clothes_extra
decoration_price = film_budget * 0.1

if extras > 150:
    price_clothes_extras = price_clothes_extras - price_clothes_extras * 0.1
else:
    price_clothes_extras = price_clothes_extras

total_price = decoration_price + price_clothes_extras
if total_price > film_budget:
    print('Not enough money!')
    print('Wingard needs ' + f'{(total_price - film_budget):.2f}' + ' leva more.')
else:
    print('Action!')
    print('Wingard starts filming with ' + f'{(film_budget - total_price):.2f}' + ' leva left.')
