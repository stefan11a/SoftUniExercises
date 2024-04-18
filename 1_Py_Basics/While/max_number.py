import sys

max_num = -sys.maxsize

while True:
    data = input()

    if data == 'Stop':
        break
    current_num = int(data)
    if current_num > max_num:
        max_num = current_num


print(max_num)