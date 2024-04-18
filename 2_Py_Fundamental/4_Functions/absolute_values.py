sequence_of_numbers = input().split()

abs_sequence = []
for j in range(len(sequence_of_numbers)):
    i = float(sequence_of_numbers[j])
    abs_sequence.append(abs(i))
print(abs_sequence)