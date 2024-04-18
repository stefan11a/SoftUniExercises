number = int(input())

odd_sum = 0
even_sum = 0

for i in range(1, number + 1):
    curr_num = int(input())

    if i % 2 == 0:
        even_sum += curr_num
    else:
        odd_sum += curr_num

if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {abs(even_sum - odd_sum)}')
