width = int(input())
length = int(input())
height = int(input())
space = width * length * height

while space > 0:
    boxes = input()

    if boxes != 'Done':
        boxes = int(boxes)
        space -= boxes
    else:
        print(f'{space} Cubic meters left.')
        break
else:
    print(f'No more free space! You need {abs(space)} Cubic meters more.')
