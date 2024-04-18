given_string = input()

rage_message = ''
repetitions = ''
current_symbols = ''

for index in range(len(given_string)):

    if not given_string[index].isdigit():
        current_symbols += given_string[index].upper()
    else:
        for next_symbols in range(index, len(given_string)):
            if not given_string[next_symbols].isdigit():
                break
            repetitions += given_string[next_symbols]
        rage_message += current_symbols * int(repetitions)
        current_symbols = ''
        repetitions = ''


print(f'Unique symbols used: {len(set(rage_message))}')
print(rage_message)
