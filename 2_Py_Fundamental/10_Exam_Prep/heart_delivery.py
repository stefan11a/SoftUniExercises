houses = [int(index) for index in input().split('@')]

curr_house = 0
command = input()

while command != 'Love!':

    line = command.split()
    jump = int(line[1])

    curr_house += jump

    if curr_house >= len(houses):
        curr_house = 0

    if houses[curr_house] - 2 == 0:
        print(f"Place {curr_house} has Valentine's day.")
        houses[curr_house] -= 2
    elif houses[curr_house] == 0:
        print(f"Place {curr_house} already had Valentine's day.")
    else:
        houses[curr_house] -= 2

    command = input()

print(f"Cupid's last position was {curr_house}.")

failed_house = 0
successful = True

for house in houses:
    if house != 0:
        successful = False
        failed_house += 1

if successful:
    print('Mission was successful.')
else:
    print(f'Cupid has failed {failed_house} places.')