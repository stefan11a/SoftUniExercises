found_plants = int(input())

plants = {}

for found_plant in range(found_plants):

    founding = input().split('<->')
    plant = founding[0]
    rarity = founding[1]

    plants[plant] = {}
    plants[plant][rarity] = []

while True:

    command = input().split(': ')

    if command[0] == 'Exhibition':
        break

    elif command[0] == 'Rate':
        line = command[1].split(' - ')
        curr_plant = line[0]
        rating = int(line[1])

        if curr_plant not in plants.keys():
            print('error')
        else:
            for rarity in plants[curr_plant].keys():
                plants[curr_plant][rarity] += [rating]

    elif command[0] == 'Update':
        line = command[1].split(' - ')
        curr_plant = line[0]
        new_rarity = line[1]
        if curr_plant not in plants.keys():
            print('error')
        else:
            for curr_rarity, curr_ratings in plants[curr_plant].items():
                plants[curr_plant] = {}
                plants[curr_plant][new_rarity] = curr_ratings

    elif command[0] == 'Reset':
        curr_plant = command[1]
        if curr_plant not in plants.keys():
            print('error')
        else:
            for curr_rarity, curr_ratings in plants[curr_plant].items():
                plants[curr_plant][curr_rarity].clear()

print('Plants for the exhibition:')

for plant in plants.keys():
    for rarity, rating in plants[plant].items():
        if len(rating) > 0:
            avg_rating = sum(rating) / len(rating)
        else:
            avg_rating = 0
        print(f'- {plant}; Rarity: {rarity}; Rating: {avg_rating:.2f}')

