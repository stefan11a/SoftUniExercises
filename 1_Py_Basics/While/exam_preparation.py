failed_threshold = int(input())
failed_times = 0
solved_tasks = 0
grades_sum = 0
last_task = ''
has_failed = True

while failed_times < failed_threshold:
    task = input()

    if task == 'Enough':
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grades_sum += grade
    solved_tasks += 1
    last_task = task

if has_failed:
    print(f'You need a break, {failed_threshold} poor grades.')
else:
    print(f'Average score: {grades_sum / solved_tasks:.2f}')
    print(f'Number of problems: {solved_tasks}')
    print(f'Last problem: {last_task}')