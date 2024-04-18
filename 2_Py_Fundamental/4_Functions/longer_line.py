from math import floor
from math import sqrt


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):

    z1 = sqrt((x1 ** 2) + (y1 ** 2))
    z2 = sqrt((x2 ** 2) + (y2 ** 2))
    z3 = sqrt((x3 ** 2) + (y3 ** 2))
    z4 = sqrt((x4 ** 2) + (y4 ** 2))

    if y1 < 0 and y2 < 0 or y1 > 0 and y2 > 0:
        s1 = sqrt(((abs(x1) + abs(x2)) ** 2) + ((abs(y1) - abs(y2)) ** 2))
    elif x1 < 0 and x2 < 0 or x1 > 0 and x2 > 0:
        s1 = sqrt(((abs(x1) - abs(x2)) ** 2) + ((abs(y1) + abs(y2)) ** 2))
    # elif x1 <= 0 <= x2 and y1 <= 0 <= y2:
    #     s1 = sqrt(((abs(x1) + abs(x2)) ** 2) + ((abs(y1) + abs(y2)) ** 2))
    # elif x1 <= 0 <= x2 and y1 <= 0 <= y2:
    #     s1 = sqrt(((abs(x1) + abs(x2)) ** 2) + ((abs(y1) + abs(y2)) ** 2))
    else:
        s1 = sqrt(((abs(x1) + abs(x2)) ** 2) + ((abs(y1) + abs(y2)) ** 2))

    if y3 < 0 and y4 < 0 or y3 > 0 and y4 > 0:
        s2 = sqrt(((abs(x3) + abs(x4)) ** 2) + ((abs(y3) - abs(y4)) ** 2))
    elif x3 < 0 and x4 < 0 or x3 > 0 and x4 > 0:
        s2 = sqrt(((abs(x3) - abs(x4)) ** 2) + ((abs(y3) + abs(y4)) ** 2))
    # elif x3 <= 0 <= x4 and y3 <= 0 <= y4:
    #     s2 = sqrt(((abs(x1) + abs(x4)) ** 2) + ((abs(y3) + abs(y4)) ** 2))
    # elif x3 <= 0 <= x4 and y3 <= 0 <= y4:
    #     s2 = sqrt(((abs(x3) + abs(x4)) ** 2) + ((abs(y3) + abs(y4)) ** 2))
    else:
        s2 = sqrt(((abs(x3) + abs(x4)) ** 2) + ((abs(y3) + abs(y4)) ** 2))

    if s1 >= s2:
        if z1 <= z2:
            return f'({floor(x1)}, {floor(y1)})({floor(x2)}, {floor(y2)})'
        else:
            return f'({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})'
    else:
        if z3 <= z4:
            return f'({floor(x3)}, {floor(y3)})({floor(x4)}, {floor(y4)})'
        else:
            return f'({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})'


X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())
X3 = float(input())
Y3 = float(input())
X4 = float(input())
Y4 = float(input())

print(longer_line(X1, Y1, X2, Y2, X3, Y3, X4, Y4))
