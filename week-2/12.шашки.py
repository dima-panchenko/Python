x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == y1 and x2 == y2:
    if y2 > y1:
        print("YES")
    else:
        print("NO")
elif (x1 % 2 == 0 and y1 % 2 == 0) and (x2 % 2 == 0 and y2 % 2 == 0):
    if y2 > y1:
        print("YES")
    else:
        print("NO")
elif (x1 % 2 == 0 and y1 % 2 == 0) and (x2 % 2 != 0 and y2 % 2 != 0):
    if y2 > y1:
        print("YES")
    else:
        print("NO")
elif (x1 % 2 != 0 and y1 % 2 != 0) and (x2 % 2 != 0 and y2 % 2 != 0):
    if y2 > y1:
        print("YES")
    else:
        print("NO")
elif (x1 % 2 != 0 and y1 % 2 != 0) and (x2 % 2 == 0 and y2 % 2 == 0):
    if y2 > y1:
        print("YES")
    else:
        print("NO")
elif (x1 % 2 == 0 and y1 % 2 != 0) and (x2 % 2 == 0 and y2 % 2 != 0):
    if y2 > y1:
        print("YES")
    else:
        print("NO")
elif (x1 % 2 == 0 and y1 % 2 != 0) and (x2 % 2 != 0 and y2 % 2 == 0):
    if y2 > y1:
        print("YES")
    else:
        print("NO")
elif (x1 % 2 != 0 and y1 % 2 == 0) and (x2 % 2 != 0 and y2 % 2 == 0):
    if y2 > y1:
        print("YES")
    else:
        print("NO")
elif (x1 % 2 != 0 and y1 % 2 == 0) and (x2 % 2 == 0 and y2 % 2 != 0):
    if y2 > y1:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
