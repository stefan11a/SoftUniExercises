def sum_numbers(n1, n2):
    return n1 + n2


def subtract(result, n3):
    return result - n3


def add_and_subtract(n1, n2, n3):
    the_sum_result = sum_numbers(n1, n2)
    final_result = subtract(the_sum_result, n3)
    return final_result


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))
