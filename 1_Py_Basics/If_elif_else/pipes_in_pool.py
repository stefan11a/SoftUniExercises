V = int(input())
P1 = int(input())
P2 = int(input())
H = float(input())

water_P1 = P1 * H
water_P2 = P2 * H

water = water_P2 + water_P1
water_p = (water / V) * 100
P1_p = (water_P1 / water) * 100
P2_p = (water_P2 / water) * 100

if V >= water:
    print('The pool is ' + f'{water_p:.2f}%' + ' full.' + ' Pipe 1: ' + f'{P1_p:.2f}%' + ' Pipe 2: ' + f'{P2_p:.2f}%.')

if water > V:
    print('For ' + f'{H}' + ' hours the pool overflows with ' + f'{(water - V)}' + ' liters.')
