some_seq = input()

check_seq = [char for char in some_seq if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

print(''.join(check_seq))
