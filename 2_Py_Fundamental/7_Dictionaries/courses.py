courses = {}

while True:

    entry_line = input()
    if entry_line == 'end':
        break
    course_name, student = entry_line.split(" : ")

    if course_name not in courses.keys():
        courses[course_name] = []
        courses[course_name].append(student)
    else:
        courses[course_name].append(student)

for curr_course in courses:
    print(f"{curr_course}: {len(courses[curr_course])}")
    for curr_student in courses[curr_course]:
        print(f'-- {curr_student}')
