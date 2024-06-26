n = int(input())

p1, p2, p3, p4, p5 = 0, 0, 0, 0, 0

for _ in range(n):
    current_num = int(input())

    if current_num < 200:
        p1 += 1
    elif 200 <= current_num <= 399:
        p2 += 1
    elif 400 <= current_num <= 599:
        p3 += 1
    elif 600 <= current_num <= 799:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

p1_sum = p1 / n * 100
p2_sum = p2 / n * 100
p3_sum = p3 / n * 100
p4_sum = p4 / n * 100
p5_sum = p5 / n * 100

print(f'{p1_sum:.2f}%')
print(f'{p2_sum:.2f}%')
print(f'{p3_sum:.2f}%')
print(f'{p4_sum:.2f}%')
print(f'{p5_sum:.2f}%')
