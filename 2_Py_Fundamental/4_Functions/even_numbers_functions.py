def is_even(number):
    return number % 2 == 0


receiving_the_sequence = list(map(int, input().split()))

filtered_list = list(filter(is_even, receiving_the_sequence))
print(filtered_list)
