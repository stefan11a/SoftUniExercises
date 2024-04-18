holidays = int(input())

working_play = (365 - holidays) * 63
holiday_play = holidays * 127
total_play = working_play + holiday_play
play = 30000

diff = abs(total_play - play)
diff_m = abs(play - total_play) % 60

if play >= total_play:
    print('Tom sleeps well')
    print(f'{diff // 60}' + ' hours and ' + f'{diff_m}' + ' minutes less for play')

else:
    print('Tom will run away')
    print(f'{diff // 60}' + ' hours and ' + f'{diff_m}' + ' minutes more for play')
