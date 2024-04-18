N1 = int(input())
N2 = int(input())

for N in range(N2, N1 - 1, -1):
    if N % N1 == 0:
        break
print(N)
