expected_amount = int(input())

card_buys = 0
cash_buys = 0
buys_count = 0
total_buys_cs = 0
total_buys_cc = 0
payment_method = ''

while expected_amount > 0:
    price = input()
    buys_count += 1
    if price != 'End':
        price = int(price)
        if buys_count % 2 == 0:
            payment_method = 'card'
        else:
            payment_method = 'cash'
        if payment_method == 'cash' and price <= 100:
            total_buys_cs += price
            cash_buys += 1
            average_cs = total_buys_cs / cash_buys
            expected_amount -= price
            print('Product sold!')
        elif payment_method == 'card' and price >= 10:
            total_buys_cc += price
            card_buys += 1
            average_cc = total_buys_cc / card_buys
            expected_amount -= price
            print('Product sold!')

        else:
            print('Error in transaction!')
    else:
        print('Failed to collect required money for charity.')
        break

else:
    print(f'Average CS: {average_cs:.2f}')
    print(f'Average CC: {average_cc:.2f}')
