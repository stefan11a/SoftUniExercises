student = input()
failed_grade = 0
years_counter = 0
grade_counter = 0

while True:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_grade += 1

        if failed_grade > 1:
            current_year = years_counter + 1
            print(f'{student} has been excluded at {years_counter + 1} grade')
            break
        continue

    else:
        grade_counter += annual_grade
        years_counter += 1

    if years_counter == 12:
        average_grade = grade_counter / 12
        print(f'{student} graduated. Average grade: {average_grade:.2f}')
        break
