some_n = int(input())
compositions = {}

for composition in range(some_n):

    some_pieces = input().split('|')
    curr_piece = some_pieces[0]
    curr_composer = some_pieces[1]
    curr_key = some_pieces[2]

    compositions[curr_piece] = {}
    compositions[curr_piece][curr_composer] = curr_key

while True:

    command = input()

    if command == 'Stop':
        break

    line = command.split('|')

    if line[0] == 'Add':
        piece = line[1]
        composer = line[2]
        key = line[3]
        if piece not in compositions.keys():
            compositions[piece] = {}
            compositions[piece][composer] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")

    elif line[0] == 'Remove':
        piece = line[1]
        if piece not in compositions.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            compositions.pop(piece)
            print(f"Successfully removed {piece}!")

    elif line[0] == 'ChangeKey':
        piece = line[1]
        new_key = line[2]
        if piece not in compositions.keys():
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            for k2, v in compositions[piece].items():
                compositions[piece][k2] = new_key
                print(f'Changed the key of {piece} to {new_key}!')

for piece in compositions.keys():
    for composer, key in compositions[piece].items():
        print(f'{piece} -> Composer: {composer}, Key: {key}')
