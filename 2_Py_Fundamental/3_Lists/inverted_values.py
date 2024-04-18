list_with_numbers = input().split()
opposite_numbers = []

for number in list_with_numbers:
    curr_num = -int(number)
    opposite_numbers.append(curr_num)
print(opposite_numbers)