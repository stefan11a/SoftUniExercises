def factorial(number1, number2):
    number1_factorial = 1
    number2_factorial = 1

    for i in range(number1, 0, -1):
        number1_factorial *= i
    for i in range(number2, 0, -1):
        number2_factorial *= i
    final_result = number1_factorial / number2_factorial
    print(f'{final_result:.2f}')


first_number = int(input())
second_number = int(input())
factorial(first_number, second_number)
