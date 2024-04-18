number = int(input())
sum_1 = 0
sum_2 = 0
for _ in range(number):
    curr_num_1 = int(input())
    sum_1 += curr_num_1
for _ in range(number):
    curr_num_2 = int(input())
    sum_2 += curr_num_2

if sum_1 == sum_2:
    print(f'Yes, sum = {sum_1}')
else:
    print(f'No, diff = {abs(sum_1 - sum_2)}')

