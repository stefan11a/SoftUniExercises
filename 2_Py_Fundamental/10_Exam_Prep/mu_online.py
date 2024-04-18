dungeon_rooms = input().split('|')

health = 100
bitcoins = 0
you_died = False
room_counter = 0

for room in dungeon_rooms:

    room_counter += 1
    room = room.split()
    command = room[0]
    amount = int(room[1])

    if command == 'potion':
        if health < 100:
            if health + amount > 100:
                healing_points = 100 - health
                health = 100
                print(f'You healed for {healing_points} hp.')
                print(f'Current health: {health} hp.')
            else:
                health = health + amount
                healing_points = amount
                print(f'You healed for {healing_points} hp.')
                print(f'Current health: {health} hp.')

    elif command == 'chest':
        bitcoins += amount
        print(f'You found {amount} bitcoins.')
    else:
        health -= amount
        if health <= 0:
            you_died = True
            print(f'You died! Killed by {command}.')
            print(f'Best room: {room_counter}')
            break
        else:
            print(f'You slayed {command}.')


if not you_died:
    print(f"You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
