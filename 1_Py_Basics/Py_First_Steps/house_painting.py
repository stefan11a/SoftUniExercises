x = float(input())
y = float(input())
h = float(input())

rear_wall = x * y
window = 1.5 * 1.5
rear_walls = 2 * rear_wall - 2 * window
back_wall = x * x
door = 2 * 1.2
fr_back_walls = back_wall * 2 - door
total_walls = fr_back_walls + rear_walls
green_paint = total_walls / 3.4

roof_walls = 2 * x * y
roof_tr = 2 * ((x * h) / 2)
total_roof = roof_tr + roof_walls
red_paint = total_roof / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
