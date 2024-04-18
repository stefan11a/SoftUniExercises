import re

some_string = input()

while some_string:

    regex = r'\d+'

    matches = re.findall(regex, some_string)
    if matches:
        print(' '.join(matches), end =' ')

    some_string = input()
