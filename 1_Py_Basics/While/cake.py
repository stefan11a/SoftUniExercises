width = int(input())
length = int(input())

total_pieces = width * length

while total_pieces > 0:
    pieces = input()

    if pieces != 'STOP':
        pieces = int(pieces)
        total_pieces -= pieces
    else:
        print(f'{total_pieces} pieces are left.')
        break
else:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')