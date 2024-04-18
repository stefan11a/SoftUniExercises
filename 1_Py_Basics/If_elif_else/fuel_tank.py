fuel = str(input())
liters = float(input())

fuel_type = 0

if fuel == 'Diesel':
    fuel_type = 'diesel'
    if liters >= 25:
        print('You have enough ' + f'{fuel_type}.')
    elif liters < 25:
        print('Fill your tank with ' + f'{fuel_type}!')

elif fuel == 'Gasoline':
    fuel_type = 'gasoline'
    if liters >= 25:
        print('You have enough ' + f'{fuel_type}.')
    elif liters < 25:
        print('Fill your tank with ' + f'{fuel_type}!')

elif fuel == 'Gas':
    fuel_type = 'gas'
    if liters >= 25:
        print('You have enough ' + f'{fuel_type}.')
    elif liters < 25:
        print('Fill your tank with ' + f'{fuel_type}!')
else:
    print('Invalid fuel!')
