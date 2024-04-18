participants = {}
submissions = {}

while True:

    entry = input().split('-')

    if len(entry) == 1:
        break

    elif len(entry) == 2:
        username = entry[0]
        del participants[username]

    elif len(entry) == 3:
        username = entry[0]
        language = entry[1]
        points = int(entry[2])

        if username not in participants.keys():
            participants[username] = 0
        if points > participants[username]:
            participants[username] = points
        if language not in submissions.keys():
            submissions[language] = 0
        submissions[language] += 1

print('Results:')
for user, points in participants.items():
    print(f'{user} | {points}')

print(f'Submissions:')
for language, submission in submissions.items():
    print(f'{language} - {submission}')
