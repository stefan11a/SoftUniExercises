some_string = input()

list_string = some_string.split(", ")

for i in list_string:
    list_string.remove('0')
    list_string.append('0')

print(list(map(int, list_string)))