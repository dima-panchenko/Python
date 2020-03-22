def IsPointInCircle(a, b, c, d, e):
    return (a - c)**2 + (b - d)**2 <= e**2


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if IsPointInCircle(x, y, xc, yc, r):
    print("YES")
else:
    print("NO")
