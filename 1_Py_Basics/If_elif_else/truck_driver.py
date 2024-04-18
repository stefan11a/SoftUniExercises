season = input()
km_monthly = float(input())

monthly_income = 0

if km_monthly <= 5000:
    if season == 'Spring' or season == 'Autumn':
        monthly_income = km_monthly * 0.75
    elif season == 'Summer':
        monthly_income = km_monthly * 0.90
    elif season == 'Winter':
        monthly_income = km_monthly * 1.05
elif 5000 < km_monthly <= 10000:
    if season == 'Spring' or season == 'Autumn':
        monthly_income = km_monthly * 0.95
    elif season == 'Summer':
        monthly_income = km_monthly * 1.10
    elif season == 'Winter':
        monthly_income = km_monthly * 1.25
else:
    monthly_income = km_monthly * 1.45

season_income = (monthly_income * 4) * 0.90

print(f'{season_income:.2f}')
