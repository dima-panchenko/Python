def distance(a, b, c, d):
    z = a - c
    n = b - d
    dis = (z**2 + n**2)**0.5
    return dis


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))
