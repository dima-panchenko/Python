a = int(input())
b = int(input())
c = int(input())
if a == b and a == c:
    print("acute")
elif a == b or a == c or b == c:
    if a + b > c and a + c > b and b + c > a:
        if a**2 + b**2 == c**2:
            print("rectangular")
        elif a**2 + c**2 == b**2:
            print("rectangular")
        elif b**2 + c**2 == a**2:
            print("rectangular")
        elif (a < b and a < c) or (b < a and b < c) or (c < a and c < b):
            print("acute")
        else:
            print("obtuse")
    else:
        print("impossible")
elif (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
    if a + b > c and a + c > b and b + c > a:
        print("rectangular")
    else:
        print("impossible")
elif (a**2 + b**2 > c**2) or (a**2 + c**2 > b**2) or (b**2 + c**2 > a**2):
    if a + b > c and a + c > b and b + c > a:
        print("obtuse")
    else:
        print("impossible")
elif (a**2 + b**2 < c**2) or (a**2 + c**2 < b**2) or (b**2 + c**2 < a**2):
    if a + b > c and a + c > b and b + c > a:
        print("acute")
    else:
        print("impossible")
else:
    print("impossible")
