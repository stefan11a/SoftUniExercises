times_poors = int(input())

current_litters = 0
capacity = 255

for i in range(times_poors):
    new_poor = int(input())
    current_litters += new_poor
    if current_litters > capacity:
        print(f'Insufficient capacity!')
        current_litters -= new_poor
print(current_litters)
