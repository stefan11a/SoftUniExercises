food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

not_enough = False

for day in range(1, 30 + 1):

    food -= 300

    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= weight / 3

    if food <= 0 or hay <= 0 or cover <= 0:
        not_enough = True
        break


food = food / 1000
hay = hay / 1000
cover = cover / 1000

if not not_enough:
    print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")
else:
    print(f'Merry must go to the pet store!')
