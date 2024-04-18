flower_type = input()
flowers = int(input())
budget = int(input())

price_change = 0
price = 0
final_price = 0

if flower_type == 'Roses' or flower_type == 'Dahlias' or flower_type == 'Tulips':

    if flower_type == 'Roses':
        price = 5
        if flowers > 80:
            price_change = 0.1
        else:
            price_change = 0

    elif flower_type == 'Dahlias':
        price = 3.80
        if flowers > 90:
            price_change = 0.15
        else:
            price_change = 0

    elif flower_type == 'Tulips':
        price = 2.80
        if flowers > 80:
            price_change = 0.15
        else:
            price_change = 0
    total_price = price * flowers
    final_price = total_price - (total_price * price_change)

elif flower_type == 'Narcissus' or flower_type == 'Gladiolus':

    if flower_type == 'Narcissus':
        price = 3
        if flowers < 120:
            price_change = 0.15
        else:
            price_change = 0

    elif flower_type == 'Gladiolus':
        price = 2.50
        if flowers < 80:
            price_change = 0.2
        else:
            price_change = 0
    total_price = price * flowers
    final_price = total_price + (total_price * price_change)

diff = abs(budget - final_price)

if budget >= final_price:
    print(f'Hey, you have a great garden with {flowers} {flower_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')

# flower_type = input()
# flowers = int(input())
# budget = int(input())
#
# total_sum = 0
#
# if flower_type == 'Roses':
#         total_sum = 5 * flowers
#         if flowers > 80:
#             total_sum = total_sum * 0.9
#
# elif flower_type == 'Dahlias':
#         total_sum = 3.80 * flowers
#         if flowers > 90:
#             total_sum = total_sum * 0.85
#
# elif flower_type == 'Tulips':
#         total_sum = 2.8 * flowers
#         if flowers > 80:
#             total_sum = total_sum * 0.85
#
# if flower_type == 'Narcissus':
#         total_sum = 3 * flowers
#         if flowers < 120:
#             total_sum = total_sum * 1.15
#
# elif flower_type == 'Gladiolus':
#         total_sum = 2.50 * flowers
#         if flowers < 80:
#             total_sum = total_sum * 1.20
#
# diff = abs(budget - total_sum)
#
# if budget >= final_price:
#     print(f'Hey, you have a great garden with {flowers} {flower_type} and {diff:.2f} leva left.')
# else:
#     print(f'Not enough money, you need {diff:.2f} leva more.')
