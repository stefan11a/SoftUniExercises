contests = {}

while True:

    command = input()

    if command == 'no more time':
        break

    username, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in contests.keys():
        contests[contest] = {}
    if username not in contests[contest]:
        contests[contest][username] = points
    elif points > contests[contest][username]:
        contests[contest][username] = points

for contest in contests.keys():
    print(f'{contest}: {len(contests[contest])} participants')
    counter = 0
    for user, points in sorted(contests[contest].items(), key=lambda cp: (-cp[1], cp[0])):
        counter += 1
        print(f'{counter}. {user} <::> {points}')

total_points_per_user = {}

for contest in contests.keys():
    for user, points in contests[contest].items():
        if user not in total_points_per_user.keys():
            total_points_per_user[user] = 0
        total_points_per_user[user] += points

print('Individual standings:')
counter2 = 0
for user, points in sorted(total_points_per_user.items(), key=lambda cp: (-cp[1], cp[0])):
    counter2 += 1
    print(f'{counter2}. {user} -> {points}')
