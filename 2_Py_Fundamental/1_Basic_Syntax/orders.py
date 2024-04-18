orders = int(input())
total_price = 0

for _ in range(orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if 0.01 <= price <= 100 and 1 <= days <= 31 and 1 <= capsules <= 2000:
        total_per_day = price * days * capsules
        print(f'The price for the coffee is: ${total_per_day:.2f}')
        total_price += total_per_day
print(f'Total: ${total_price:.2f}')
