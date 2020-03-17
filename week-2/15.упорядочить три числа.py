a = int(input())
b = int(input())
c = int(input())
if b < a and b < c:
    (a, b) = (b, a)
    if c < b:
        (b, c) = (c, b)
elif c < a and c < b:
    (a, c) = (c, a)
    if c < b:
        (b, c) = (c, b)
elif a > b and a > c:
    (c, a) = (a, c)
    if b < a:
        (a, b) = (b, a)
else:
    if c < b:
        (b, c) = (c, b)
print(a, b, c)
