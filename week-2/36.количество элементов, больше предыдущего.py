num = int(input())
maxN = num
col = 0
while num != 0:
    num = int(input())
    if num > maxN:
        maxN = num
        col += 1
    else:
        maxN = num
print(col)
