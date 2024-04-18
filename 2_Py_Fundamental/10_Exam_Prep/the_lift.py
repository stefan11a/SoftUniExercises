number_of_people = int(input())

lift = [int(curr_lift) for curr_lift in input().split()]

for index in range(len(lift)):
    while lift[index] < 4:
        lift[index] += 1
        number_of_people -= 1
        if number_of_people == 0:
            break

for curr_lift in range(len(lift)):
    if lift[curr_lift] < 4:
        print('The lift has empty spots!')
        print(' '.join(map(str, lift)))
        break
else:
    if number_of_people > 0:
        print(f"There isn't enough space! {number_of_people} people in a queue!")
    print(' '.join(map(str, lift)))
