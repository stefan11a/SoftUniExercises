climbers_groups = int(input())

total_climbers = 0
p1 , p2, p3, p4, p5= 0, 0, 0, 0, 0

for _ in range(climbers_groups):
    climbers_per_group = int(input())
    total_climbers += climbers_per_group

    if climbers_per_group <= 5:
        p1 += climbers_per_group
    elif 6 <= climbers_per_group <= 12:
        p2 += climbers_per_group
    elif 13 <= climbers_per_group <= 25:
        p3 += climbers_per_group
    elif 26 <= climbers_per_group <= 40:
        p4 += climbers_per_group
    elif climbers_per_group >= 41:
        p5 += climbers_per_group

p1_ratio = (p1 / total_climbers) * 100
p2_ratio = (p2 / total_climbers) * 100
p3_ratio = (p3 / total_climbers) * 100
p4_ratio = (p4 / total_climbers) * 100
p5_ratio = (p5 / total_climbers) * 100

print(f'{p1_ratio:.2f}%')
print(f'{p2_ratio:.2f}%')
print(f'{p3_ratio:.2f}%')
print(f'{p4_ratio:.2f}%')
print(f'{p5_ratio:.2f}%')
