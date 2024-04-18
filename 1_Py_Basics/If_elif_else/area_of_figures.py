from math import pi
figure = str(input())
area = 0

if figure == 'square':
    x = float(input())
    area = x * x
    print(f'{area:.3f}')
elif figure == 'rectangle':
    x = float(input())
    y = float(input())
    area = x * y
    print(f'{area:.3f}')
elif figure == 'circle':
    x = float(input())
    area = (x ** 2) * pi
    print(f'{area:.3f}')
elif figure == 'triangle':
    x = float(input())
    y = float(input())
    area = x * y / 2
    print(f'{area:.3f}')
