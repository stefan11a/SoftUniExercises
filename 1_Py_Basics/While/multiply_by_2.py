a = float(input())

if a < 0:
    print('Negative number!')
while a >= 0:
    print(f'Result: {a * 2:.2f}')
    a = float(input())
    if a < 0:
        print('Negative number!')
        break
