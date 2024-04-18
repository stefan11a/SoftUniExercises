budget = float(input())
season = input()

place = ''
location = ''
price = 0

if budget <= 1000:
    place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000:
    place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60
else:
    place = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
    elif season == 'Winter':
        location = 'Morocco'
    price = budget * 0.90

print(f'{location} - {place} - {price:.2f}')
