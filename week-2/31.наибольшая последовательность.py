num = int(input())
num2 = num
coll = 0
maxColl = 0
while num != 0:
    num = int(input())
    if num2 == num:
        coll += 1
    elif num2 != num:
        num2 = num
        if coll > maxColl:
            maxColl = coll
        coll = 0
print(maxColl + 1)
