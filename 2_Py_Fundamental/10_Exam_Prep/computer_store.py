total_price = 0

is_special = False

while True:

    command = input()

    if command == 'special':
        is_special = True
        break
    elif command == 'regular':
        break

    price = float(command)
    if price < 0:
        print(f'Invalid price!')
    else:
        total_price += price


if total_price != 0:
    taxed_price = total_price * 1.2
    taxes = total_price * 0.2
    if is_special:
        final_price = taxed_price * 0.9
    else:
        final_price = taxed_price
    print(f"Congratulations you've just bought a new computer!"
          f"\nPrice without taxes: {total_price:.2f}$"
          f"\nTaxes: {taxes:.2f}$"
          f"\n-----------"
          f"\nTotal price: {final_price:.2f}$")
else:
    print('Invalid order!')
