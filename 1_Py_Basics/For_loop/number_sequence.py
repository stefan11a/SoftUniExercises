from sys import maxsize
n = int(input())

max_number = -maxsize
min_number = maxsize

for _ in range(n):
    current_num = int(input())

    if current_num > max_number:
        max_number = current_num
    if current_num < min_number:
        min_number = current_num

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
