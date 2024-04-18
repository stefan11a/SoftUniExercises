def length_validator(some_username):
    if 3 <= len(some_username) <= 16:
        return True
    return False


def characters_validator(some_username):
    for char in some_username:
        if not (char.isalnum()
                or char == '-'
                or char == '_'):
            return False
    return True


def redundant_validator(some_username):
    if ' ' in some_username:
        return False
    return True


def isvalid(some_username):
    if length_validator(some_username)\
            and characters_validator(some_username)\
            and redundant_validator(some_username):
        return True
    return False


usernames = input().split(', ')

for username in usernames:
    if isvalid(username):
        print(username)
