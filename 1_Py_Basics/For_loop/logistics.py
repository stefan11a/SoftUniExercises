cargo = int(input())

vehicle_type = ''
price1, price2, price3 = 0, 0, 0
tones1, tones2, tones3 = 0, 0, 0
total_tones = 0

for each_cargo in range(cargo):
    tones = int(input())
    total_tones += tones
    if tones <= 3:
        tones1 += tones
        price1 += tones * 200
    elif 4 <= tones <= 11:
        tones2 += tones
        price2 += tones * 175
    elif tones >= 12:
        tones3 += tones
        price3 += tones * 120

average_price = (price1 + price2 + price3) / total_tones
tones1_sum = tones1 / total_tones * 100
tones2_sum = tones2 / total_tones * 100
tones3_sum = tones3 / total_tones * 100

print(f'{average_price:.2f}')
print(f'{tones1_sum:.2f}%')
print(f'{tones2_sum:.2f}%')
print(f'{tones3_sum:.2f}%')
