N1 = int(input())
N2 = int(input())
operation = input()

result = 0
type_of_result = 0
zero_flag = False

if operation == '+':
    result = N1 + N2
elif operation == '-':
    result = N1 - N2
elif operation == '*':
    result = N1 * N2
elif operation == '/':
    if N2 == 0:
        zero_flag = True
    else:
        result = N1 / N2

elif operation == '%':
    if N2 == 0:
        zero_flag = True
    else:
        result = N1 % N2

if operation == '+' or operation == '-' or operation == '*':
    if result % 2 == 0:
        type_of_result = 'even'
    else:
        type_of_result = 'odd'
    print(f'{N1} {operation} {N2} = {result} - {type_of_result}')

elif operation == '/':
    if zero_flag:
        print(f'Cannot divide {N1} by zero')
    else:
        print(f'{N1} / {N2} = {result:.2f}')
elif operation == '%':
    if zero_flag:
        print(f'Cannot divide {N1} by zero')
    else:
        print(f'{N1} % {N2} = {result}')
