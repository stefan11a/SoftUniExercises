resources = {}

while True:
    curr_resource = input()
    if curr_resource == 'stop':
        break

    curr_quantity = int(input())
    if curr_resource not in resources.keys():
        resources[curr_resource] = 0
    resources[curr_resource] += curr_quantity

for curr_resources in resources:
    print(f"{curr_resources} -> {resources[curr_resources]}")

# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")