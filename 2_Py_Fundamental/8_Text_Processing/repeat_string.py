some_str = input().split()
result = [the_str * len(the_str) for the_str in some_str]
print(''.join(result))