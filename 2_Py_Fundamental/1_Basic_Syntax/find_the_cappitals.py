some_string = input()

list_string = [*some_string]
uppers_list = []
index = len(list_string)
for k in range(65, 91):
    for i in range(index):
        if chr(k) == list_string[i]:
            uppers_list.append(i)
print(sorted(uppers_list))
