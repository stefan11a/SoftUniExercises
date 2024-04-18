season = input()
group = input()
students = int(input())
nights = int(input())

price = 0
sport = ''
total_price = 0

if group == 'boys' or group == 'girls':
    if season == 'Winter':
        price = students * 9.60
    elif season == 'Spring':
        price = students * 7.20
    elif season == 'Summer':
        price = students * 15
elif group == 'mixed':
    if season == 'Winter':
        price = students * 10
    elif season == 'Spring':
        price = students * 9.50
    elif season == 'Summer':
        price = students * 20

final_price = price * nights

if students >= 50:
    total_price = final_price * 0.50
elif 20 <= students < 50:
    total_price = final_price * 0.85
elif 10 <= students < 20:
    total_price = final_price * 0.95
else:
    total_price = final_price

if season == 'Winter':
    if group == 'girls':
        sport = 'Gymnastics'
    elif group == 'boys':
        sport = 'Judo'
    elif group == 'mixed':
        sport = 'Ski'
if season == 'Spring':
    if group == 'girls':
        sport = 'Athletics'
    elif group == 'boys':
        sport = 'Tennis'
    elif group == 'mixed':
        sport = 'Cycling'
if season == 'Summer':
    if group == 'girls':
        sport = 'Volleyball'
    elif group == 'boys':
        sport = 'Football'
    elif group == 'mixed':
        sport = 'Swimming'

print(f'{sport} {total_price:.2f} lv.')
