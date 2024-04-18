from math import ceil
from math import floor

days = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

turtle_food_kg = turtle_food / 1000

eaten_food = dog_food * days + cat_food * days + turtle_food_kg * days

if food >= eaten_food:
    print(f'{floor(food - eaten_food)}' + ' kilos of food left.')
elif food < eaten_food:
    print(f'{ceil(eaten_food - food)}' + ' more kilos of food are needed.')
