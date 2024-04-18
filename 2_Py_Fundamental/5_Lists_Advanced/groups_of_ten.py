numbers = [int(number) for number in input().split(", ")]

current_group = 10
while numbers:
    filtered_number_for_curr_group = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_number_for_curr_group}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_number_for_curr_group]
