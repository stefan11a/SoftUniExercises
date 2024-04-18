n = int(input())
positive = []
negative = []
for i in range(n):
    number = int(input())
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')