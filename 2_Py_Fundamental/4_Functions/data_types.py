def reading_string(some_string, some_data):
    if some_string == 'int':
        return int(some_data) * 2
    elif some_string == 'real':
        return f'{float(some_data) * 1.5:.2f}'
    elif some_string == 'string':
        return f'${some_data}$'


data = input()
second_data = input()

print(reading_string(data, second_data))
