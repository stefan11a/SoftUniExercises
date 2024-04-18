vacation_price = float(input())
budget = float(input())
spend_count = 0
days_count = 0

while budget < vacation_price:
    action = input()
    funds = float(input())

    if action == 'spend':
        if budget <= funds:
            funds = budget
        budget -= funds
        spend_count += 1
        days_count += 1
        if spend_count > 4:
            print('You can\'t save the money.')
            print(days_count)
            break
    elif action == 'save':
        budget += funds
        days_count += 1
        spend_count = 0

else:
    print(f'You saved the money for {days_count} days.')
