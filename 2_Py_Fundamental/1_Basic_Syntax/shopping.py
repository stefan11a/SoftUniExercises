budget = int(input())
n = input()

while n != 'End':
    n = int(n)
    budget -= n
    if budget < 0:
        print('You went in overdraft!')
        break
    n = input()
else:
    print('You bought everything needed.')