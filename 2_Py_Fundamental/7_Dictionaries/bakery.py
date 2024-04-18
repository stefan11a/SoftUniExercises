products_information = input().split()

food_storage = {}

for i in range(0, len(products_information), 2):
    food = products_information[i]
    quantity = products_information[i + 1]
    food_storage[food] = int(quantity)

print(food_storage)