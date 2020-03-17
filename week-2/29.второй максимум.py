num = int(input())
max1 = num
max2 = 0
while num != 0:
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif max2 < num <= max1:
        max2 = num
print(max2)
