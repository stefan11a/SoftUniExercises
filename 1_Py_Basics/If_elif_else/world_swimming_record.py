record = float(input())
distance_m = float(input())
time_per_m = float(input())

resistance = (distance_m // 15) * 12.5
final_time = time_per_m * distance_m
total_time = final_time + resistance

if record > total_time:
    print('Yes, he succeeded! The new world record is ' + f'{total_time:.2f}' + ' seconds.')
else:
    print('No, he failed! He was ' + f'{(total_time - record):.2f}' + ' seconds slower.')
