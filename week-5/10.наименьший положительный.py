numList = list(map(int, input().split()))
i = 0
k = 1000
while i < len(numList):
    if numList[i] > 0:
        if numList[i] < k:
            k = numList[i]
    i += 1
print(k)
