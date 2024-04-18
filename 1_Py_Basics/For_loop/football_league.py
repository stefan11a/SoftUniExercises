capacity = int(input())
fans = int(input())

A, B, V, G = 0, 0, 0, 0

for _ in range(1, fans + 1):
    sector = input()
    if sector == 'A':
        A += 1
    elif sector == 'B':
        B += 1
    elif sector == 'V':
        V += 1
    elif sector == 'G':
        G += 1
fans_p = fans / capacity * 100

A_p = A / fans * 100
B_p = B / fans * 100
V_p = V / fans * 100
G_p = G / fans * 100

print(f'{A_p:.2f}%')
print(f'{B_p:.2f}%')
print(f'{V_p:.2f}%')
print(f'{G_p:.2f}%')
print(f'{fans_p:.2f}%')
