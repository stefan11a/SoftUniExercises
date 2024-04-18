predefined_string = input()
password = ''
while True:

    command = input().split(' ')

    if command[0] == 'Done':
        print(f'Your password is: {password}')
        break

    elif command[0] == 'TakeOdd':
        for i in range(0, len(predefined_string)):
            if i % 2 != 0:
                password += predefined_string[i]
        print(password)

    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        substring = password[index: index + length]
        password = password.replace(substring, '', 1)
        print(password)

    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print('Nothing to replace!')
