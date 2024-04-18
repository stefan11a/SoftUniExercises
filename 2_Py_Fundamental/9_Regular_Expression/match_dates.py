import re

text = input()

# For use in another directory
valid_dates =[]

# RegEx validator
date_validator = r'(\d{2})([./-])([A-Z][a-z]{2})\2(\d{4})'

# RegEx function
matches = re.findall(date_validator, text)

for match in matches:
    day = match[0]
    month = match[2]
    year = match[3]
    print(f'Day: {day}, Month: {month}, Year: {year}')


# Here we iterate trough the the input and search the matches by groups
# matches = re.finditer(date_validator, text)
#
# for match in matches:
#     day = match.group(1)
#     month = match.group(2)
#     year = match.group(3)
#     print(f'Day: {day}, Month: {month}, Year: {year}')
