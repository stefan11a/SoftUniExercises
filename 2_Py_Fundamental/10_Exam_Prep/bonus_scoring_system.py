number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

list_of_attendances = []

for student in range(number_of_students):
    attendance_per_student = int(input())

    student_bonus = (attendance_per_student / number_of_lectures) * (5 + additional_bonus)
    list_of_attendances.append([round(student_bonus), attendance_per_student])

curr_max = 0
att = 0
for max_value, value in list_of_attendances:

    if max_value > curr_max:
        curr_max = max_value
        att = value

print(f'Max Bonus: {curr_max}.')
print(f'The student has attended {att} lectures.')
