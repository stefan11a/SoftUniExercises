products_information = input().split()
search_products = input().split()

storage = {}

for i in range(0, len(products_information), 2):
    food = products_information[i]
    quantity = products_information[i + 1]
    storage[food] = quantity

for j in search_products:
    if j in storage:
        print(f"We have {storage[j]} of {j} left")
    else:
        print(f"Sorry, we don't have {j}")
