n = int(input())
numbers_list = []
filtered = []

for i in range(n):
    new_n = int(input())
    numbers_list.append(new_n)
command = input()
if command == 'even':
    for new_n in numbers_list:
        if new_n % 2 == 0:
            filtered.append(new_n)
elif command == 'odd':
    for new_n in numbers_list:
        if new_n % 2 != 0:
            filtered.append(new_n)
elif command == 'negative':
    for new_n in numbers_list:
        if new_n < 0:
            filtered.append(new_n)
elif command == 'positive':
    for new_n in numbers_list:
        if new_n >= 0:
            filtered.append(new_n)

print(filtered)