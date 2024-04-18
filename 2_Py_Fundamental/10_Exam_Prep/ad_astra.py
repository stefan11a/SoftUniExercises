import re

text = input()

pattern = r'#[a-zA-Z ]+#[0-9/]+#[0-9]+#|[|][a-zA-Z ]+[|][0-9/]+[|][0-9]+[|]'

total_calories = 0

matches = re.findall(pattern, text)

for match in matches:
    if '#' in match:
        match = match.split('#')
    else:
        match = match.split('|')
    calories = int(match[3])
    total_calories += calories

days_to_last = total_calories // 2000

print(f'You have food to last you for: {days_to_last} days!')

for match in matches:
    if '#' in match:
        match = match.split('#')
    else:
        match = match.split('|')
    item = match[1]
    date = match[2]
    calories = match[3]

    print(f'Item: {item}, Best before: {date}, Nutrition: {calories}')

