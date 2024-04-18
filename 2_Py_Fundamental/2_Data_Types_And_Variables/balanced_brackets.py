n = int(input())
stack = []

left_stack = 0
right_stack = 0
flag = False

for _ in range(n):
    line = input()
    if line == "(":
        stack.append('(')
        left_stack += 1
        if left_stack > 1:
            break
    elif line == ")":
        if stack:
            stack.pop()
            left_stack -= 1
            flag = True
        else:
            stack.append(')')
            break

if not stack:
    print("BALANCED")
else:
    print("UNBALANCED")
