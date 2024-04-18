number_1 = int(input())
number_2 = int(input())

for count in range(number_1, number_2 + 1):
    curr_num = str(count)

    odd_sum = 0
    even_sum = 0
    for j in range(0, len(curr_num)):
        digit = int(curr_num[j])
        if j % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if odd_sum == even_sum:
        print(count, end=' ')
