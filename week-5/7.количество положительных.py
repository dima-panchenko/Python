numList = list(map(int, input().split()))
i = 0
col = 0
while i < len(numList):
    if numList[i] > 0:
        col += 1
    i += 1
print(col)
