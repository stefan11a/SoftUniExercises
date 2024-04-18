products_information = {}

while True:

    entry = input()

    if entry == 'buy':
        break

    product, price, quantity = entry.split()
    price = float(price)
    quantity = int(quantity)

    if product in products_information:
        old_price, old_quantity = products_information[product]
        total_quantity = old_quantity + quantity

        if old_price != price:
            products_information[product] = (price, total_quantity)
        else:
            products_information[product] = (old_price, total_quantity)
    else:
        products_information[product] = (price, quantity)

for the_products, (the_prices, the_quantity) in products_information.items():
    final_price = the_prices * the_quantity
    print(f'{the_products} -> {final_price:.2f}')
