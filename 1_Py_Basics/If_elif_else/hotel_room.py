month = input()
nights = int(input())

studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77

if 7 < nights <= 14 and (month == 'May' or month == 'October'):
    studio = studio * 0.95
    apartment = apartment
elif nights > 14 and (month == 'May' or month == 'October'):
    studio = studio * 0.70
    apartment = apartment * 0.9
elif nights > 14 and (month == 'June' or month == 'September'):
    studio = studio * 0.8
    apartment = apartment * 0.9
elif nights > 14 and (month == 'July' or month == 'August'):
    studio = studio
    apartment = apartment * 0.9
studio_price = nights * studio
apartment_price = nights * apartment

print(f'Apartment: {apartment_price:.2f} lv.')
print(f'Studio: {studio_price:.2f} lv.')
