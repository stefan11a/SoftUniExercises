budget = float(input())
season = input()

price = 0
holiday_place = ""
holiday_type = ""

if budget <= 100:
    holiday_place = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
        holiday_type = 'Camp'
    elif season == 'winter':
        price = budget * 0.7
        holiday_type = 'Hotel'

elif budget <= 1000:
    holiday_place = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
        holiday_type = 'Camp'
    elif season == 'winter':
        price = budget * 0.8
        holiday_type = 'Hotel'

elif budget > 1000:
    holiday_place = 'Europe'
    price = budget * 0.9
    holiday_type = 'Hotel'

print(f'Somewhere in {holiday_place}')
print(f'{holiday_type} - {price:.2f}')
