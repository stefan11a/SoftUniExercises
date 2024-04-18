number_of_heroes = int(input())

heroes = {}

max_hp = 100
max_mp = 200

for number_of_hero in range(number_of_heroes):

    hero = input().split()
    name = hero[0]
    HP = hero[1]
    MP = hero[2]

    heroes[name] = {}
    heroes[name][HP] = MP

while True:

    command = input().split(' - ')

    if command[0] == 'End':
        break

    elif command[0] == 'CastSpell':
        curr_hero = command[1]
        hp = heroes[curr_hero]
        mp = int(command[2])
        spell = command[3]

        for hp, curr_mp in heroes[curr_hero].items():
            if mp < int(curr_mp):
                curr_mp = int(curr_mp) - mp
                heroes[curr_hero][hp] = curr_mp
                print(f"{curr_hero} has successfully cast {spell} and now has {curr_mp} MP!")
            else:
                print(f'{curr_hero} does not have enough MP to cast {spell}!')

    elif command[0] == 'TakeDamage':
        curr_hero = command[1]
        damage = int(command[2])
        attacker = command[3]

        for hp, curr_mp in heroes[curr_hero].items():
            hp = int(hp) - damage
            if hp > 0:
                print(f'{curr_hero} was hit for {damage} HP by {attacker} and now has {hp} HP left!')
            else:
                print(f'{curr_hero} has been killed by {attacker}!')
        heroes[curr_hero] = {}
        heroes[curr_hero][hp] = curr_mp

    elif command[0] == 'Recharge':
        curr_hero = command[1]
        amount = int(command[2])

        for hp, curr_mp in heroes[curr_hero].items():
            if int(curr_mp) + amount > max_mp:
                recovered_mp = max_mp - int(curr_mp)
                heroes[curr_hero] = {}
                heroes[curr_hero][hp] = max_mp
            else:
                recovered_mp = amount
                heroes[curr_hero] = {}
                heroes[curr_hero][hp] = int(curr_mp) + amount
        print(f'{curr_hero} recharged for {recovered_mp} MP!')

    elif command[0] == 'Heal':
        curr_hero = command[1]
        amount = int(command[2])

        for hp, curr_mp in heroes[curr_hero].items():
            if int(hp) + amount > max_hp:
                recovered_hp = max_hp - int(hp)
                heroes[curr_hero] = {}
                heroes[curr_hero][max_hp] = curr_mp
            else:
                recovered_hp = amount
                hp = int(hp) + amount
                heroes[curr_hero] = {}
                heroes[curr_hero][hp] = curr_mp
        print(f'{curr_hero} healed for {recovered_hp} HP!')

for curr_hero in heroes.keys():
    for hp, mp in heroes[curr_hero].items():
        if int(hp) > 0:
            print(f'{curr_hero}')
            print(f'  HP: {hp}')
            print(f'  MP: {mp}')
