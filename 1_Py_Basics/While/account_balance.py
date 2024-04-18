balance = 0

while True:
    data = input()

    if data == 'NoMoreMoney':
        break
    current_balance = float(data)
    if current_balance >= 0:
        balance += current_balance
        print(f'Increase: {current_balance:.2f}')
    else:
        print('Invalid operation!')
        break
print(f'Total: {balance:.2f}')
