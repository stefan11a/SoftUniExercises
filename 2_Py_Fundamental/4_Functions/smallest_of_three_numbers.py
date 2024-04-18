def three_integers(the_list):
    return min(the_list)


open_list = []
for i in range(3):
    number = int(input())
    open_list.append(number)

print(three_integers(open_list))
