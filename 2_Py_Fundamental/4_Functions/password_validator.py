def password_check(given_password):
    length = 6 <= len(given_password) <= 10
    letter_digits = False
    for j in given_password:
        if 48 <= ord(j) <= 57 or 65 <= ord(j) <= 90 or 97 <= ord(j) <= 122:
            letter_digits = True
        else:
            letter_digits = False
            break
    two_digits = False
    count_digits = 0
    for i in given_password:
        if 48 <= ord(i) <= 57:
            count_digits += 1
            if count_digits == 2:
                two_digits = True
                break

    if length and letter_digits and two_digits:
        print('Password is valid')
    else:
        if not length:
            print("Password must be between 6 and 10 characters")
        if not letter_digits:
            print("Password must consist only of letters and digits")
        if not two_digits:
            print("Password must have at least 2 digits")


password = input()

password_check(password)