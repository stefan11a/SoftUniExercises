import sys

numbers = int(input())

min_num = sys.maxsize
max_num = -sys.maxsize
odd_sum = 0
even_sum = 0

for i in range(numbers):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print(f'OddSum={odd_sum:.2f},')
print(f'EvenSum={even_sum:.2f},')

for _ in range(numbers):
    if num > max_num:
        max_num = num
        print(f'OddMax={max_num:.2f},')
    else:
        print(f'OddMax=No,')
    if num < min_num:
        min_num = num
        print(f'OddMax={max_num:.2f},')
    else:
        print(f'OddMin=No,')

    if num > max_num:
        max_num = num
        print(f'EvenMax={max_num:.2f},')
    else:
        print(f'EvenMax=No,')
    if num < min_num:
        min_num = num
        print(f'EvenMin={min_num:.2f},')
    else:
        print(f'EvenMax=No')


# print(f'OddMax={max_num:.2f},')
# print(f'OddMax=No,')
# print(f'OddMin={min_num:.2f},')
# print(f'OddMin=No,')
# print(f'EvenMax={max_num:.2f},')
# print(f'EvenMax=No,')
# print(f'EvenMin={min_num:.2f},')
# print(f'EvenMax=No')
