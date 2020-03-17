num = int(input())
sumN = 0
col = 0
while num != 0:
    sumN += num
    col += 1
    num = int(input())
print(sumN / col)
