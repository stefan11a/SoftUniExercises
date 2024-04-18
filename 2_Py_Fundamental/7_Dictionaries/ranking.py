contests = {}
submissions = {}

while True:

    entry_line = input()

    if entry_line == 'end of contests':
        break

    contest, password = entry_line.split(':')
    contests[contest] = password

while True:

    entry = input()

    if entry == 'end of submissions':
        break

    contest, password, username, points = entry.split('=>')
    points = int(points)
    if contest in contests.keys():
        if password in contests[contest]:
            if username not in submissions.keys():
                submissions[username] = {}
            if contest not in submissions[username]:
                submissions[username][contest] = points
            elif points > submissions[username][contest]:
                submissions[username][contest] = points

total_points_per_user = {user: sum(points.values()) for user, points in submissions.items()}

best_user = max(total_points_per_user, key=total_points_per_user.get)
best_user_points = total_points_per_user[best_user]

print(f'Best candidate is {best_user} with total {best_user_points} points.')
print('Ranking:')
for user in sorted(submissions.keys()):
    print(user)
    for contest, points in sorted(submissions[user].items(), key=lambda cp: -cp[1]):
        print(f'#  {contest} -> {points}')

