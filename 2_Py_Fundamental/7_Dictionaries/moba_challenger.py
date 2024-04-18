moba_players = {}

while True:

    entry = input()
    if entry == 'Season end':
        break

    if '->' in entry:
        player, position, skill = entry.split(' -> ')
        skill = int(skill)

        if player not in moba_players.keys():
            moba_players[player] = {}
        if position not in moba_players[player] or skill > moba_players[player][position]:
            moba_players[player][position] = skill

    elif ' vs ' in entry:
        player1, player2 = entry.split(' vs ')
        if player1 in moba_players and player2 in moba_players:
            for position in moba_players[player1]:
                if position in moba_players[player2]:
                    if moba_players[player1][position] > moba_players[player2][position]:
                        del moba_players[player2]
                    elif moba_players[player1][position] < moba_players[player2][position]:
                        del moba_players[player1]

total_points_per_plr = {}

for player in moba_players.keys():
    for position, skills in moba_players[player].items():
        if player not in total_points_per_plr.keys():
            total_points_per_plr[player] = 0
        total_points_per_plr[player] += skills

for player, points in sorted(total_points_per_plr.items(), key=lambda pp: -pp[1]):
    print(f'{player}: {points} skill')
    for position, skills in sorted(moba_players[player].items(), key=lambda ps: -ps[1]):
        print(f'- {position} <::> {skills}')
