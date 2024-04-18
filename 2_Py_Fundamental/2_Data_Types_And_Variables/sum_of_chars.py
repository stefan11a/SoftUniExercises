letters = int(input())
total_sum = 0

for i in range(letters):
    curr_letter = input()
    total_sum += ord(curr_letter)

print(f'The sum equals: {total_sum}')