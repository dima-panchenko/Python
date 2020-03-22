def IsPointInSquare(a, b):
    return abs(a) + abs(b) <= 1


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
