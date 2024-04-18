n = int(input())
word = input()
strings = []

for i in range(n):
    current_str = input()
    strings.append(current_str)
print(strings)
for b in range(len(strings) - 1, -1, -1):
    element = strings[b]
    if word not in element:
        strings.remove(element)
print(strings)
