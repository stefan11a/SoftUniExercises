from math import floor
from math import ceil
X = int(input())
Y = float(input())
Z = int(input())
workers = int(input())

grape = Y * X
wine_grape = grape * 0.4
wine = wine_grape / 2.5

if wine < Z:
    print('It will be a tough winter! More ' + f'{floor(Z - wine)}' + ' liters wine needed.')
if wine >= Z:
    print('Good harvest this year! Total wine: ' + f'{(floor(wine))}' + ' liters.')
    print(f'{(ceil(wine - Z))}' + ' liters left -> ' + f'{ceil((wine - Z) / workers)}' + ' liters per person.')
