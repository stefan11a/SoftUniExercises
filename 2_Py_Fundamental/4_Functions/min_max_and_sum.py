def min_of(the_list):
    return min(the_list)


def max_of(the_list):
    return max(the_list)


def sum_of(the_list):
    return sum(the_list)


num_seq = list(map(int, input().split()))

print(f"The minimum number is {min_of(num_seq)}")
print(f"The maximum number is {max_of(num_seq)}")
print(f"The sum number is: {sum_of(num_seq)}")
