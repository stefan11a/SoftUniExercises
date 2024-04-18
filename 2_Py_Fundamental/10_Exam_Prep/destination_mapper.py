import re

places_on_map = input()
total_points = 0

pattern = r'=[A-Z][a-zA-Z]+=|/[A-Z][a-zA-Z]+/'

matches = re.findall(pattern, places_on_map)

valid = []

for match in matches:
    match = match[1:-1]
    if len(match) > 3:
        valid.append(match)

    total_points += len(match)

if len(valid) > 0:
    print(f"Destinations: {', '.join(valid)}")
else:
    print("Destinations:")
print(f'Travel Points: {total_points}')
