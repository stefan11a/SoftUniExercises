from math import floor


def coordinates(x1, y1, x2, y2):
    if abs(x1) <= abs(x2) and abs(y1) <= abs(y2):
        return f'({floor(x1)}, {floor(y1)})'
    else:
        return f'({floor(x2)}, {floor(y2)})'


X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())

print(coordinates(X1, Y1, X2, Y2))
