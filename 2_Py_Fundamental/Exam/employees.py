import re

number_of_lines = int(input())

for line in range(number_of_lines):

    employee_info = input()

    pattern = r'([A-Z][a-z]{3,} [A-Z][a-z]{3,})#+([A-Za-z&]+)\d{2}([A-Z][a-z]+ [Ltd.|JSC]+)'

    matches = re.findall(pattern, employee_info)

    for match in matches:
        if '&&' not in match[1]:
            job = match[1].split('&')
            name = match[0]
            company = match[2]
            print(f"{name} is {' '.join(job)} at {company}")
