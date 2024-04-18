H = int(input())
R = int(input())
T = int(input())
season = input()
holiday = input()

H_price = 0
R_price = 0
T_price = 0

if season == 'Spring' or season == 'Summer':
    if holiday == 'Y':
        H_price = 2 * 1.15
        R_price = 4.1 * 1.15
        T_price = 2.5 * 1.15
    elif holiday == 'N':
        H_price = 2
        R_price = 4.1
        T_price = 2.5
elif season == 'Autumn' or season == 'Winter':
    if holiday == 'Y':
        H_price = 3.75 * 1.15
        R_price = 4.5 * 1.15
        T_price = 4.15 * 1.15
    elif holiday == 'N':
        H_price = 3.75
        R_price = 4.5
        T_price = 4.15

bouquet = H * H_price + R * R_price + T * T_price
total_f = H + R + T

if T > 7 and season == 'Spring':
    bouquet = bouquet * 0.95
if R >= 10 and season == 'Winter':
    bouquet = bouquet * 0.9
if total_f > 20:
    bouquet = bouquet * 0.8

final_price = bouquet + 2

print(f'{final_price:.2f}')
