floors = int(input())
rooms = int(input())
room_type = ''

for f_count in reversed(range(1, floors + 1)):
    if f_count % 2 == 0:
        room_type = 'O'
    else:
        room_type = 'A'
    if f_count == floors:
        room_type = 'L'
    for r_count in range(0, rooms):
        print(f'{room_type}{f_count}{r_count}', end=' ')
    print('')
