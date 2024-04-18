def calculation(number1, number2, operator):

    if operator == 'multiply':
        return number1 * number2
    elif operator == 'divide':
        return int(number1 / number2)
    elif operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2


some_operator = input()
N1 = int(input())
N2 = int(input())

print(calculation(N1, N2, some_operator))
