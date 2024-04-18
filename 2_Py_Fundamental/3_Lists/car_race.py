from math import ceil
the_sequence = input().split()

left_car_time = 0
right_car_time = 0

for index in range(len(the_sequence)):
    middle_index = len(the_sequence) // 2
    left_car = the_sequence[0:middle_index]
    right_car = the_sequence[-1:middle_index:-1]

for left_index in range(len(left_car)):
    left_car_time += int(left_car[left_index])
    if int(left_car[left_index]) == 0:
        left_car_time = left_car_time * 0.8

for right_index in range(len(right_car)):
    right_car_time += int(right_car[right_index])
    if int(right_car[right_index]) == 0:
        right_car_time = right_car_time * 0.8

if right_car_time < left_car_time:
    print(f'The winner is right with total time: {right_car_time:.1f}')
elif left_car_time < right_car_time:
    print(f'The winner is left with total time: {left_car_time:.1f}')
