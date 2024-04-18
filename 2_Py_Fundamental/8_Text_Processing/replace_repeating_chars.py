text = input()
final_text = ''
last_added_char = ''
for char in text:
    if last_added_char != char:
        final_text += char
        last_added_char = char
print(final_text)