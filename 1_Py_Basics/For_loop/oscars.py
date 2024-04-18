actor_name = input()
points_academy = float(input())
jury = int(input())

points = points_academy

for _ in range(jury):
    jury_name = input()
    jury_points = float(input())
    points += len(jury_name) * jury_points / 2
    if points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!')
        break
else:
    print(f'Sorry, {actor_name} you need {(1250.5 - points):.1f} more!')
