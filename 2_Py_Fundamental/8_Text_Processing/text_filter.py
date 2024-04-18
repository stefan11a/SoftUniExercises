banned_words = input().split(', ')
some_string = input()

for word in banned_words:
    while word in some_string:
        some_string = some_string.replace(word, "*" * len(word))

print(some_string)