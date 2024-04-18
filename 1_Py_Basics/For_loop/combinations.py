n = int(input())
combo_counts = 0

for i in range(0, n + 1):
    for u in range(0, n + 1):
        for k in range(0, n + 1):
            if i + u + k == n:
                combo_counts += 1

print(combo_counts)