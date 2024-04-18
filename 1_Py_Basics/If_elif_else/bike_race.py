juniors = int(input())
seniors = int(input())
track = input()

juniors_tax = 0
seniors_tax = 0

if track == 'trail':
    juniors_tax = 5.5
    seniors_tax = 7
elif track == 'cross-country':
    juniors_tax = 8
    seniors_tax = 9.5
elif track == 'downhill':
    juniors_tax = 12.25
    seniors_tax = 13.75
elif track == 'road':
    juniors_tax = 20
    seniors_tax = 21.5

competitors = juniors + seniors
total_tax = juniors * juniors_tax + seniors * seniors_tax
collected_money = 0

if competitors >= 50 and track == 'cross-country':
    collected_money = (total_tax * 0.75) * 0.95
else:
    collected_money = total_tax * 0.95

print(f'{collected_money:.2f}')