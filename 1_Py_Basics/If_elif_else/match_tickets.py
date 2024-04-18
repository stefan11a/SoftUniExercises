budget = float(input())
category = input()
group = int(input())

remaining_budget = 0
total_price = 0

if 1 <= group <= 4:
    remaining_budget = budget * 0.25
elif 5 <= group <= 9:
    remaining_budget = budget * 0.40
elif 10 <= group <= 24:
    remaining_budget = budget * 0.50
elif 25 <= group <= 49:
    remaining_budget = budget * 0.60
elif group >= 50:
    remaining_budget = budget * 0.75

if category == 'VIP':
    total_price = group * 499.99
elif category == 'Normal':
    total_price = group * 249.99

remaining_balance = abs(remaining_budget - total_price)

if remaining_budget >= total_price:
    print(f'Yes! You have {remaining_balance:.2f} leva left.')
else:
    print(f'Not enough money! You need {remaining_balance:.2f} leva.')
