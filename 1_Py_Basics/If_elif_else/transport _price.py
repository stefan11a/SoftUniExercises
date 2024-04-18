n = int(input())
time = str(input())

if time == 'day':
        taxi = 0.7 + (n * 0.79)
        bus = n * 0.09
        train = n * 0.06
elif time == 'night':
        taxi = 0.7 + (n * 0.9)
        bus = n * 0.09
        train = n * 0.06
if n < 20:
    print(f'{taxi:.2f}')
elif n < 100:
    print(f'{bus:.2f}')
elif n >= 100:
    print(f'{train:.2f}')
