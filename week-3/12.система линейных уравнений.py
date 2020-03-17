a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
if a == 0 and d == 0:
    print(f, e)
else:
    y = (f - ((c * e) / a)) / (d - ((b * c) / a))
    x = (e - b * y) / a
    print(x, y)
