turns = int(input())

result = 0
number_count_1, number_count_2, number_count_3, number_count_4, number_count_5, number_count_6 = 0, 0, 0, 0, 0, 0

for all_turns in range(1, turns + 1):
    number = int(input())
    if 0 <= number < 10:
        result += number * 0.2
        number_count_1 += 1
    elif 10 <= number < 20:
        result += number * 0.3
        number_count_2 += 1
    elif 20 <= number < 30:
        result += number * 0.4
        number_count_3 += 1
    elif 30 <= number < 40:
        result += 50
        number_count_4 += 1
    elif 40 <= number <= 50:
        result += 100
        number_count_5 += 1
    else:
        result /= 2
        number_count_6 += 1

number_count_1_sum = number_count_1 / turns * 100
number_count_2_sum = number_count_2 / turns * 100
number_count_3_sum = number_count_3 / turns * 100
number_count_4_sum = number_count_4 / turns * 100
number_count_5_sum = number_count_5 / turns * 100
number_count_6_sum = number_count_6 / turns * 100

print(f'{result:.2f}')
print(f'From 0 to 9: {number_count_1_sum:.2f}%')
print(f'From 10 to 19: {number_count_2_sum:.2f}%')
print(f'From 20 to 29: {number_count_3_sum:.2f}%')
print(f'From 30 to 39: {number_count_4_sum:.2f}%')
print(f'From 40 to 50: {number_count_5_sum:.2f}%')
print(f'Invalid numbers: {number_count_6_sum:.2f}%')
