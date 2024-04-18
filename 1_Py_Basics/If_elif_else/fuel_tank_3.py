fuel = str(input())
liters = float(input())
card = str(input())

fuel_price = 0

if fuel == 'Gasoline':
    fuel_price = 2.22
    if card == 'Yes':
        fuel_price = fuel_price - 0.18
        if liters < 20:
            total = liters * fuel_price
            print(f'{total:.2f} lv.')
        elif liters <= 25:
            total = liters * fuel_price - (liters * fuel_price * 0.08)
            print(f'{total:.2f} lv.')
        elif liters > 25:
            total = liters * fuel_price - (liters * fuel_price * 0.1)
            print(f'{total:.2f} lv.')

    elif card == 'No':
        fuel_price = 2.22
        if liters < 20:
            total = liters * fuel_price
            print(f'{total:.2f} lv.')
        elif liters <= 25:
            total = liters * fuel_price - (liters * fuel_price * 0.08)
            print(f'{total:.2f} lv.')
        elif liters > 25:
            total = liters * fuel_price - (liters * fuel_price * 0.1)
            print(f'{total:.2f} lv.')

elif fuel == 'Diesel':
    fuel_price = 2.33
    if card == 'Yes':
        fuel_price = fuel_price - 0.12
        if liters < 20:
            total = liters * fuel_price
            print(f'{total:.2f} lv.')
        elif liters <= 25:
            total = liters * fuel_price - (liters * fuel_price * 0.08)
            print(f'{total:.2f} lv.')
        elif liters > 25:
            total = liters * fuel_price - (liters * fuel_price * 0.1)
            print(f'{total:.2f} lv.')

    elif card == 'No':
        fuel_price = 2.33
        if liters < 20:
            total = liters * fuel_price
            print(f'{total:.2f} lv.')
        elif 20 <= liters <= 25:
            total = liters * fuel_price - (liters * fuel_price * 0.08)
            print(f'{total:.2f} lv.')
        elif liters > 25:
            total = liters * fuel_price - (liters * fuel_price * 0.1)
            print(f'{total:.2f} lv.')

elif fuel == 'Gas':
    fuel_price = 0.93
    if card == 'Yes':
        fuel_price = fuel_price - 0.08
        if liters < 20:
            total = liters * fuel_price
            print(f'{total:.2f} lv.')

        elif liters <= 25:
            total = liters * fuel_price - (liters * fuel_price * 0.08)
            print(f'{total:.2f} lv.')
        elif liters > 25:
            total = liters * fuel_price - (liters * fuel_price * 0.1)
            print(f'{total:.2f} lv.')

    elif card == 'No':
        fuel_price = 0.93
        if liters < 20:
            total = liters * fuel_price
            print(f'{total:.2f} lv.')
        elif liters <= 25:
            total = liters * fuel_price - (liters * fuel_price * 0.08)
            print(f'{total:.2f} lv.')
        elif liters > 25:
            total = liters * fuel_price - (liters * fuel_price * 0.1)
            print(f'{total:.2f} lv.')
