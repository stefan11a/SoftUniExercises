soldiers = input().split()
k = int(input())
killed_soldiers = []
bullet = 0

while len(soldiers) > 0:
    index = 0
    while index < len(soldiers):
        bullet += 1
        if bullet == k:
            killed_soldiers.append(soldiers[index])
            del soldiers[index]
            bullet = 0
        else:
            index += 1
killed_soldiers = ','.join(killed_soldiers)
print(f'[{killed_soldiers}]')
