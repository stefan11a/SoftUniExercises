n = int(input())
total_sum = 0

for i in range(n):
    number = int(input())
    total_sum += number

average = total_sum / n
print(f'{average:.2f}')