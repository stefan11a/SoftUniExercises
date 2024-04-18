numbers = int(input())


previous_sum = 0
max_diff = 0
have_diff = False

for num in range(1, numbers + 1):
    N1 = int(input())
    N2 = int(input())
    current_sum = N1 + N2
    if not previous_sum:
        previous_sum = current_sum
    else:
        diff = abs(previous_sum - current_sum)
        if diff > max_diff:
            max_diff = diff
            have_diff = True
        if diff:
            previous_sum = current_sum

if have_diff:
    print(f'No, maxdiff={diff}')
else:
    print(f'Yes, value={current_sum}')
