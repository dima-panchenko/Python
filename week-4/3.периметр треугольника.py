def distance(a, b, c, d):
    z = a - c
    n = b - d
    dis = (z**2 + n**2)**0.5
    return dis


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
side1 = distance(x1, y1, x2, y2)
side2 = distance(x2, y2, x3, y3)
side3 = distance(x3, y3, x1, y1)
print(side1 + side2 + side3)
