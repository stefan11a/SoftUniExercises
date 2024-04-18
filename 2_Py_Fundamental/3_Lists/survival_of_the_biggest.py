integers_list = input().split()
numbers_to_remove = int(input())

for i in range(0, len(integers_list)):
    integers_list[i] = int(integers_list[i])
for number in range(numbers_to_remove):
    integers_list.remove(min(integers_list))
current_list = map(str, integers_list)
print(', '.join(current_list))