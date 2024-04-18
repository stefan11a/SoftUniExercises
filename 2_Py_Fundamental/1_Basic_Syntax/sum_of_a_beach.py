a = input().lower()
some_words = ["Sand", "Water", "Fish", "Sun"]
counter = 0

for word in some_words:
    if word.lower() in a:
        something = word.lower()
        count = a.count(something)
        counter += count
print(counter)
