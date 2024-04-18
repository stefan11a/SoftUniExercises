import re

text = input()

# For use in another directory is required
valid_phones = []

# RegEx validation
valid_phone = r'\+359-2-[0-9]{3}-[0-9]{4}\\b|\+359 2 [0-9]{3} [0-9]{4}\\b'

# RegEx function
matches = re.findall(valid_phone, text)

print(', '.join(matches))
