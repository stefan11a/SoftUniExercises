all_stops = input()

while True:

    command = input().split(':')

    if command[0] == 'Travel':
        break

    elif command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]

        if 0 <= index < len(all_stops):
            all_stops = all_stops[:index] + string + all_stops[index:]
        print(all_stops)

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(all_stops) and 0 <= end_index < len(all_stops):
            substring = all_stops[start_index:end_index + 1]
            all_stops = all_stops.replace(substring, '', 1)
        print(all_stops)

    elif command[0] == 'Switch':
        old_string = command[1]
        new_string = command[2]

        if old_string in all_stops:
            all_stops = all_stops.replace(old_string, new_string)
        print(all_stops)

print(f'Ready for world tour! Planned stops: {all_stops}')
