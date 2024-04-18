days = int(input())
total_plunder = 0
plunder_per_day = int(input())

for curr_day in range(1, days + 1):

    total_plunder += plunder_per_day

    if curr_day % 3 == 0:
        total_plunder += plunder_per_day * 0.5
    if curr_day % 5 == 0:
        total_plunder = total_plunder * 0.7

expected_plunder = int(input())
collected_plunder = (total_plunder / expected_plunder) * 100

if total_plunder >= expected_plunder:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
else:
    print(f'Collected only {collected_plunder:.2f}% of the plunder.')
