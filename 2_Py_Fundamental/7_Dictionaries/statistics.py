stock = {}

while True:

    line = input()

    if line == 'statistics':
        break

    product, quantity = line.split(": ")
    quantity = int(quantity)

    if product in stock:
        stock[product] += int(quantity)
    else:
        stock[product] = int(quantity)

products_in_stock = len(stock)
total_quantity = sum(stock.values())
print('Products in stock:')

for product, quantity in stock.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {products_in_stock}')
print(f'Total Quantity: {total_quantity}')
