key = int(input())
N = int(input())

code_list = []

for i in range(N):
    letter = input()
    letter_plus_key = ord(letter) + key
    new_letter = chr(letter_plus_key)
    code_list.append(new_letter)

print(''.join(code_list))
