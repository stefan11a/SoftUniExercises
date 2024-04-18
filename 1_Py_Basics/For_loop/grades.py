students = int(input())

top_students = 0
good_students = 0
average_students = 0
bad_students = 0
grade_sum = 0

for each_student in range(students):
    grade = float(input())
    grade_sum += grade
    if 2 <= grade < 3.00:
        bad_students += 1
    elif 3 <= grade < 4:
        average_students += 1
    elif 4 <= grade < 5:
        good_students += 1
    elif grade >= 5:
        top_students += 1

average_grade = grade_sum / students

bad_students_sum = bad_students / students * 100
average_students_sum = average_students / students * 100
good_students_sum = good_students / students * 100
top_students_sum = top_students / students * 100

print(f'Top students: {top_students_sum:.2f}%')
print(f'Between 4.00 and 4.99: {good_students_sum:.2f}%')
print(f'Between 3.00 and 3.99: {average_students_sum:.2f}%')
print(f'Fail: {bad_students_sum:.2f}%')
print(f'Average: {average_grade:.2f}')
