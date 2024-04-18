herd = input()

herd_list = herd.split(", ")
reversed_herd_list = list(reversed(herd_list))

if reversed_herd_list.index('wolf') == 0:
    print('Please go away and stop eating my sheep')

if reversed_herd_list.index('wolf') != 0:
    sheep = reversed_herd_list.index('wolf')
    print(f'Oi! Sheep number {sheep}! You are about to be eaten by a wolf!')