skill = input()

while True:

    command = input().split()

    if command[0] == 'For' and command[1] == 'Azeroth':
        break

    elif command[0] == 'GladiatorStance':
        skill = skill.upper()
        print(skill)

    elif command[0] == 'DefensiveStance':
        skill = skill.lower()
        print(skill)

    elif command[0] == 'Dispel':
        index = int(command[1])
        letter = command[2]
        new_skill = ''
        if 0 <= index < len(skill):
            for i in range(len(skill)):
                if i == index:
                    new_skill += letter
                else:
                    new_skill += skill[i]
            skill = new_skill
            print('Success!')

        else:
            print('Dispel too weak.')

    elif command[1] == 'Change':
        first_substring = command[2]
        second_substring = command[3]
        skill = skill.replace(first_substring, second_substring)
        print(skill)

    elif command[1] == 'Remove':
        substring = command[2]
        if substring in skill:
            skill = skill.replace(substring, '', 1)
            print(skill)

    else:
        print("Command doesn't exist!")

