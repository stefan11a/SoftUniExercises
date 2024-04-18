inheritance = float(input())
year_to_live = int(input())

years_old = 0

for year in range(1800, year_to_live + 1):
    years_old = 18 + year % 1800
    if year % 2 == 0:
        inheritance -= 12000
    else:
        inheritance -= 12000 + (50 * years_old)

if inheritance >= 0:
    print(f'Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.')
else:
    print(f'He will need {(abs(inheritance)):.2f} dollars to survive.')
