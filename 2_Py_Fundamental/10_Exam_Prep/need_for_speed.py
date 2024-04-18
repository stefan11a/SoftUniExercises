number_of_cars = int(input())
cars = {}

tank_max = 75

for number in range(number_of_cars):

    car = input().split('|')
    car_model = car[0]
    mileage = car[1]
    fuel = car[2]

    cars[car_model] = {}
    cars[car_model][int(mileage)] = int(fuel)

while True:

    command = input().split(' : ')
    is_sold = False

    if command[0] == 'Stop':
        break

    elif command[0] == 'Drive':
        curr_car = command[1]
        curr_distance = int(command[2])
        required_fuel = int(command[3])

        for distance, available_fuel in cars[curr_car].items():
            if required_fuel > available_fuel:
                print('Not enough fuel to make that ride')
            else:
                total_mileage = distance + curr_distance
                cars[curr_car] = {}
                cars[curr_car][total_mileage] = available_fuel - required_fuel
                print(f'{curr_car} driven for {curr_distance} kilometers. {required_fuel} liters of fuel consumed.')

                if total_mileage > 100000:
                    print(f'Time to sell the {curr_car}!')
                    is_sold = True
                    del cars[curr_car]

    elif command[0] == 'Refuel':
        curr_car = command[1]
        curr_fuel = int(command[2])

        for distance, fuel in cars[curr_car].items():
            if fuel + curr_fuel > tank_max:
                refueled_fuel = tank_max - fuel
                cars[curr_car] = {}
                cars[curr_car][distance] = tank_max
            else:
                refueled_fuel = curr_fuel
                cars[curr_car] = {}
                cars[curr_car][distance] = curr_fuel + fuel
        print(f'{curr_car} refueled with {refueled_fuel} liters')

    elif command[0] == 'Revert':
        curr_car = command[1]
        kilometers = int(command[2])

        for distance, fuel in cars[curr_car].items():
            if distance - kilometers < 10000:
                final_distance = 10000
                cars[curr_car] = {}
                cars[curr_car][final_distance] = fuel
            else:
                final_distance = distance - kilometers
                cars[curr_car] = {}
                cars[curr_car][final_distance] = fuel
                print(f'{curr_car} mileage decreased by {kilometers} kilometers')

for car in cars.keys():
    for final_mileage, final_fuel in cars[car].items():
        print(f'{car} -> Mileage: {final_mileage} kms, Fuel in the tank: {final_fuel} lt.')
