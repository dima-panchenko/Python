num = int(input())
max1 = num
i = 0
while num != 0:
    num = int(input())
    if num > max1:
        max1 = num
        i = 0
    elif num == max1:
        i += 1
print(i + 1)
