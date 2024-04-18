def total_price(product, quantity):
    if product == 'coffee':
        return f'{quantity * 1.5:.2f}'
    elif product == 'water':
        return f'{quantity * 1:.2f}'
    elif product == 'coke':
        return f'{quantity * 1.4:.2f}'
    elif product == 'snacks':
        return f'{quantity * 2:.2f}'


the_product = input()
the_quantity = int(input())

print(total_price(the_product, the_quantity))