text = input()
encrypted_txt = ''
for char in text:
    encrypted_txt += chr(ord(char) + 3)
print(encrypted_txt)
