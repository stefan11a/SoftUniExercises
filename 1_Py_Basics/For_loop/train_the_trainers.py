jury = int(input())
presentation = input()

sum_all_grades = 0
count_all_grades = 0

while presentation != 'Finish':

    sum_grades = 0
    for i in range(1, jury + 1):
        grade = float(input())
        sum_all_grades += grade
        sum_grades += grade
        count_all_grades += 1
    average_grade = sum_grades / jury
    print(f'{presentation} - {average_grade:.2f}.')

    presentation = input()

avg_all_grade = sum_all_grades / count_all_grades
print(f'Student\'s final assessment is {avg_all_grade:.2f}.')
