numList = list(map(int, input().split()))
i = 0
while i < len(numList):
    if i % 2 == 0:
        print(numList[i], end=" ")
    i += 1
