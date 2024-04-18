destination = input()
min_budget = float(input())
current_budget = 0
is_end = False
has_budget = False

while destination != 'End':
    while current_budget < min_budget:
        budget = float(input())
        current_budget += budget
        if current_budget >= min_budget:
            print(f'Going to {destination}!')
            current_budget = 0
            has_budget = True
            if has_budget:
                destination = input()
                if destination == 'End':
                    is_end = True
                    break
                min_budget = float(input())
        if is_end:
            break
