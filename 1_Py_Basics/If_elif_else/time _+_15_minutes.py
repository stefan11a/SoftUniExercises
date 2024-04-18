hours = int(input())
minutes = int(input())

bonus_time = 15
minutes_bonus = bonus_time + minutes

if minutes_bonus > 59:
    hours = hours + 1
    minutes_bonus = minutes_bonus - 60

if hours > 23:
    hours = 0

if minutes_bonus < 10:
    print(f'{hours}:0{minutes_bonus}')
else:
    print(f'{hours}:{minutes_bonus}')
