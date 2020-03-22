def IsPointInSquare(a, b):
    return -1 <= a <= 1 and -1 <= b <= 1


x = float(input())
y = float(input())
if IsPointInSquare(x, y):
    print("YES")
else:
    print("NO")
