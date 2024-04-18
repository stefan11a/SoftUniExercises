encrypted_msg = list(input())
command = input()

while command != 'Decode':

    command = command.split('|')

    if 'Move' in command:
        letter_to_move = int(command[1])
        for counter in range(letter_to_move):
            encrypted_msg.append(encrypted_msg[0])
            encrypted_msg.pop(0)
    elif 'Insert' in command:
        letter_to_insert = command[2]
        position = int(command[1])
        encrypted_msg.insert(position, letter_to_insert)
    elif 'ChangeAll' in command:
        letter_to_change = command[1]
        new_letter = command[2]
        encrypted_msg = [sub.replace(letter_to_change, new_letter) for sub in encrypted_msg]

    command = input()

print(f"The decrypted message is: {''.join(encrypted_msg)}")
