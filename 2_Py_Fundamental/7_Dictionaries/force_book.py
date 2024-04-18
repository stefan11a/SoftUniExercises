force_users = {}

entry = input()
while True:

    if entry == 'Lumpawaroo':
        break

    if ' | ' in entry:
        force_side, force_user = entry.split(' | ')
        user_is_part_of_the_force = False
        for value in force_users.values():
            if force_user in value:
                user_is_part_of_the_force = True
                break
        if not user_is_part_of_the_force:
            if force_side not in force_users.keys():
                force_users[force_side] = []
            force_users[force_side].append(force_user)

    elif ' -> ' in entry:
        force_user, force_side = entry.split(' -> ')

        for value in force_users.values():
            if force_user in value:
                value.remove(force_user)
                break
        if force_side not in force_users.keys():
            force_users[force_side] = []
        force_users[force_side].append(force_user)
        print(f'{force_user} joins the {force_side} side!')

    entry = input()

for side, users in force_users.items():
    if len(users) > 0:
        print(f'Side: {side}, Members: {len(users)}')
        for the_users in force_users[side]:
            print(f"! {the_users}")
