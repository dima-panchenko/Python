numList = list(map(int, input().split()))
i = 1
k = numList[0]
while i < len(numList):
    if numList[i] > k:
        k = numList[i]
        print(numList[i], end=" ")
    else:
        k = numList[i]
    i += 1
