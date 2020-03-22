def IsPointInArea(x, y):
    a = (x + 1) ** 2 + (y - 1) ** 2 <= 4 and y >= -x and y >= 2 * x + 2
    b = (x + 1) ** 2 + (y - 1) ** 2 >= 4 and y <= -x and y <= 2 * x + 2
    return a or b


x = float(input())
y = float(input())
if IsPointInArea(x, y):
    print("YES")
else:
    print("NO")
