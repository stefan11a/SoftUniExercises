from math import ceil
name = str(input())
time = int(input())
break_time = int(input())

lunch_time = 0.125 * break_time
brb_time = 0.25 * break_time

free_time = break_time - (lunch_time + brb_time)

if free_time >= time:
    print('You have enough time to watch ' + name + ' and left with ' + str(ceil((free_time - time))) +
          ' minutes free time.')
else:
    print("You don't have enough time to watch " + name + ', you need ' + str(ceil((time - free_time))) +
          ' more minutes.')
