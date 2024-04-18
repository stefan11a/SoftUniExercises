given_numbers = input().split()

the_numbers = []
for i in range(len(given_numbers)):
    j = float(given_numbers[i])
    the_numbers.append(round(j))

print(the_numbers)
