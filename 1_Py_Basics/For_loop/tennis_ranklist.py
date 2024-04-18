tournaments = int(input())
starting_points = int(input())

points = starting_points
won_tourneys = 0

for _ in range(tournaments):
    stage = input()
    if stage == 'W':
        points += 2000
        won_tourneys += 1
    elif stage == 'F':
        points += 1200
    elif stage == 'SF':
        points += 720

average_points = (points - starting_points) // tournaments
won_tourneys_sum = won_tourneys / tournaments * 100

print(f'Final points: {points}')
print(f'Average points: {average_points}')
print(f'{won_tourneys_sum:.2f}%')
