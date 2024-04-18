number_of_electrons = int(input())

shells = []

for shell in range(1, number_of_electrons + 1):
    max_electrons_curr_shell = 2 * shell ** 2
    if number_of_electrons >= max_electrons_curr_shell:
        shells.append(max_electrons_curr_shell)
        number_of_electrons -= max_electrons_curr_shell
        if number_of_electrons == 0:
            break
    else:
        shells.append(number_of_electrons)
        break

print(shells)