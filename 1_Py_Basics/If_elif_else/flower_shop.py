from math import ceil
from math import floor

M = int(input())
Z = int(input())
R = int(input())
C = int(input())
gift_prize = float(input())

M_prize = M * 3.25
Z_prize = Z * 4
R_prize = R * 3.5
C_prize = C * 8

total_prize = M_prize + Z_prize + R_prize + C_prize
winnings = total_prize - total_prize * 0.05

if gift_prize <= winnings:
    print('She is left with ' + f'{floor(winnings - gift_prize)}' + ' leva.')
elif gift_prize > winnings:
    print('She will have to borrow ' + f'{ceil(gift_prize - winnings)}' + ' leva.')
