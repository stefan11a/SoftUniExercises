projection = input()
r = int(input())
c = int(input())

income = 0

if projection == 'Premiere':
    income = 12
elif projection == 'Normal':
    income = 7.50
elif projection == 'Discount':
    income = 5

total_income = income * r * c
print(f'{total_income:.2f} leva')
