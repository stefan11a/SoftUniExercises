import re

name = input()
matched_names = [] #For use in different directory

#RegEx pattern to validate the names
pattern = '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b'

#The validator
valid_name = re.findall(pattern, name)

for matches in valid_name:
    print(matches, end=' ')