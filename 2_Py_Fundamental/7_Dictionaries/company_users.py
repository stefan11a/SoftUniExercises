companies = {}

while True:

    entry_line = input()
    if entry_line == 'End':
        break
    company, employee = entry_line.split(" -> ")

    if company not in companies.keys():
        companies[company] = [employee]
    else:
        if employee not in companies[company]:
            companies[company].append(employee)


for curr_company in companies:
    print(f"{curr_company}")
    for curr_employee in companies[curr_company]:
        print(f'-- {curr_employee}')
