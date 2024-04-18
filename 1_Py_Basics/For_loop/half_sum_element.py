import sys

number = int(input())
total_sum = 0
max_number = -sys.maxsize


for num in range(number):
    current_num = int(input())
    total_sum += current_num

    if current_num > max_number:
        max_number = current_num

if total_sum - max_number == max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(max_number - (total_sum - max_number))
    print('No')
    print(f'Diff = {diff}')
