grade_book = {}

students = int(input())

for student in range(students):

    name = input()
    grade = float(input())

    if name not in grade_book.keys():
        grade_book[name] = [grade]
    else:
        grade_book[name].append(grade)

for curr_student, grades in grade_book.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f'{curr_student} -> {average_grade:.2f}')
