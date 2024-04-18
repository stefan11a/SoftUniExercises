n1 = int(input())
n2 = int(input())
mn = int(input())
count = 0
loop_condition = False

for i in range(n1, n2 + 1):
    for u in range(n1, n2 + 1):
        count += 1

        if i + u == mn:
            print(f'Combination N:{count} ({i} + {u} = {mn})')
            loop_condition = True
            break
    if loop_condition:
        break
else:
    print(f'{count} combinations - neither equals {mn}')
