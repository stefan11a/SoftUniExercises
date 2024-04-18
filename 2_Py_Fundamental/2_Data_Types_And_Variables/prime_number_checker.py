N = int(input())

flag = False
if N == 1:
    print(False)
elif N > 1:
    for i in range(2, N):
        if N % i == 0:
            flag = True
            break
if flag:
    print('False')
else:
    print('True')