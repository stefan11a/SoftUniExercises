status_of_p_ship = [int(status) for status in input().split('>')]
status_of_w_ship = [int(status) for status in input().split('>')]

max_hp_per_section = int(input())

is_sunken = False

line = input()

while not line == 'Retire':

    command = line.split()

    if command[0] == 'Fire':
        index = int(command[1])
        damage_to_w = int(command[2])
        if index in range(len(status_of_w_ship)):
            status_of_w_ship[index] = status_of_w_ship[index] - damage_to_w

            if status_of_w_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_sunken = True
                break

    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage_to_p = int(command[3])
        if start_index in range(len(status_of_p_ship)) and end_index in range(len(status_of_p_ship)):
            for curr_section in range(start_index, end_index + 1):
                status_of_p_ship[curr_section] = status_of_p_ship[curr_section] - damage_to_p
                if status_of_p_ship[curr_section] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    is_sunken = True
                    break

    elif command[0] == 'Repair':
        rep_index = int(command[1])
        health = int(command[2])
        if rep_index in range(len(status_of_p_ship)):
            if status_of_p_ship[rep_index] + health > max_hp_per_section:
                status_of_p_ship[rep_index] = max_hp_per_section
            else:
                status_of_p_ship[rep_index] += health

    elif command[0] == 'Status':
        need_repair_count = 0
        for curr_sec in range(len(status_of_p_ship)):
            need_repair = max_hp_per_section * 0.2
            if status_of_p_ship[curr_sec] < need_repair:
                need_repair_count += 1
        print(f'{need_repair_count} sections need repair.')

    line = input()

if not is_sunken:
    print(f"Pirate ship status: {sum(status_of_p_ship)}")
    print(f"Warship status: {sum(status_of_w_ship)}")
