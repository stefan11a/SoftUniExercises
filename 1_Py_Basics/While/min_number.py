import sys

min_num = sys.maxsize

while True:
    data = input()

    if data == 'Stop':
        break
    current_num = int(data)
    if current_num < min_num:
        min_num = current_num

print(min_num)