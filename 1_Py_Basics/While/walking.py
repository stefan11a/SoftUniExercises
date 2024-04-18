goal = 10000
steps = 0

while steps < goal:
    steps_per_walk = input()

    if steps_per_walk != 'Going home':
        steps_per_walk = int(steps_per_walk)
        steps += steps_per_walk
    else:
        steps_to_home = int(input())
        steps += steps_to_home
        diff_goal = abs(goal - steps)
        if steps >= goal:
            print('Goal reached! Good job!')
            print(f'{diff_goal} steps over the goal!')
            break
        else:
            print(f'{diff_goal} more steps to reach goal.')
            break

else:
    diff_goal = abs(goal - steps)
    print(f'Goal reached! Good job!')
    print(f'{diff_goal} steps over the goal!')
