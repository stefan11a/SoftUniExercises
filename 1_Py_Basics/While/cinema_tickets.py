input_line = input()

count_standard = 0
count_students = 0
count_kids = 0
total_count = 0

while input_line != 'Finish':
    movie = input_line
    capacity = int(input())

    count_tickets = 0
    command_line = input()
    while command_line != 'End':
        type_ticket = command_line
        count_tickets += 1

        if type_ticket == 'standard':
            count_standard += 1
        elif type_ticket == 'student':
            count_students += 1
        elif type_ticket == 'kid':
            count_kids += 1

        if count_tickets == capacity:
            break

        command_line = input()

    total_count += count_tickets

    percent_filled_capacity = count_tickets / capacity * 100
    print(f'{movie} - {percent_filled_capacity:.2f}% full.')

    input_line = input()

print(f'Total tickets: {total_count}')
percent_standard = count_standard / total_count * 100
percent_student = count_students / total_count * 100
percent_kid = count_kids / total_count * 100
print(f'{percent_student:.2f}% student tickets.')
print(f'{percent_standard:.2f}% standard tickets.')
print(f'{percent_kid:.2f}% kids tickets.')
